import os
import kopf
import kubernetes
import yaml
import asyncio
import time
import requests
import json
import pandas as pd


CARBON_INTENSITY_API_URL = os.getenv("CARBON_INTENSITY_API_URL", default="https://og-serverless.azure-api.net/electricitymaphack/findBestContinuousTimeSlot")

# utility func
def findBestContinuousTimeSlot(jobEarliestStart, jobDeadline, jobDuration, location):
    
    api_request = '%s?jobEarliestStart=%s&jobDeadline=%s&jobDuration=%s&zone=%s' % (CARBON_INTENSITY_API_URL, jobEarliestStart, jobDeadline, jobDuration, location)
    
    response = requests.get(api_request)

    json_data = response.json() if response and response.status_code == 200 else None
    bestStartTime = json_data['bestStartTime'] if json_data and 'bestStartTime' in json_data else None

    print("API call: FindBestContinuousTimeSlot : jobEarliestStart=%s&jobDeadline=%s&jobDuration=%s&zone=%s" % (jobEarliestStart, jobDeadline, jobDuration, location))

    print("FindBestContinuousTimeSlot results: %s" % json_data)

    return bestStartTime 


# utility func
def findMatchingCronJobTimeScheduler(cronjobnamespace, cronjoblabels):

    api = kubernetes.client.CustomObjectsApi()
    cronJobTimeSchedulersList = api.list_namespaced_custom_object(
        group="carbon-aware-actions.kubernetes",
        version="dev",
        namespace=cronjobnamespace,
        plural="cronjobtimeschedulers",
    )     

    for cronjobtimescheduler in cronJobTimeSchedulersList["items"]:
        targetCronJobLabels = cronjobtimescheduler["spec"]["cronJobRef"]["labels"]
        for key in cronjoblabels:
            if ((key in targetCronJobLabels) and (cronjoblabels[key] == targetCronJobLabels[key])):  #if cronjob labels match as a taget for CronJobTimeScheduler Operator
                return cronjobtimescheduler
    
    return None


###############################

def doBestTimeEstimation(cronJobtimescheduler):

    jobDuration = cronJobtimescheduler["spec"]["jobDuration"]

    location = cronJobtimescheduler["spec"]["location"]

    timezone = cronJobtimescheduler["spec"]["timezone"]


    jobDeadline_hour_minute = cronJobtimescheduler["spec"]["jobDeadline"]
    jobEarliestStart_hour_minute = cronJobtimescheduler["spec"]["jobEarliestStart"]

    #figure out the days corresponding to earliest start and deadline: today or tomorrow

    currentTime = pd.Timestamp.now(tz='UTC')

    jobDeadline = pd.Timestamp(jobDeadline_hour_minute, tz=timezone).tz_convert('UTC')

    jobEarliestStart = pd.Timestamp(jobEarliestStart_hour_minute, tz=timezone).tz_convert('UTC')
    
    #if deadline is 09:00; and current time is 20:00 => job deadline is in the following day


    if currentTime >= jobEarliestStart : jobEarliestStart = jobEarliestStart + pd.Timedelta(days=1)  
    jobEarliestStart_string = jobEarliestStart.strftime('%Y-%m-%d %X')

    if currentTime >= jobDeadline : jobDeadline = jobDeadline + pd.Timedelta(days=1)  

    #increment Deadline by 1 more day if the conversion of hour:minutes to timestamp if deadline is in the following day
    if jobEarliestStart >= jobDeadline: jobDeadline = jobDeadline + pd.Timedelta(days=1)  
    jobDeadline_string = jobDeadline.strftime('%Y-%m-%d %X')

    # find Best time to schedule job, based on the constraints expressed in the jobTimeScheduler CRD
    bestStartTime = findBestContinuousTimeSlot(jobEarliestStart_string, jobDeadline_string, jobDuration, location)

    if bestStartTime is None :
        print("API call findBestContinuousTimeSlot returned None => using EarliestStart to schedule Job") 
        return jobEarliestStart_hour_minute 


    return bestStartTime


##############################
#When CronJob is created/updated, annotate CronJob and findBestTime in the future to schedule the next Job occurence
@kopf.on.create('cronjobs') 
def AnnotateCronJobAndScheduleNextJob(body, spec, name, namespace, status, annotations, labels, **kwargs):


    # find Matching cronJobTimeScheduler for current Job
    cronJobtimescheduler = findMatchingCronJobTimeScheduler(namespace, labels) 
    if cronJobtimescheduler is None : return # No TimeScheduler found, do nothing
    

    # find Best time to schedule job, based on the constraints expressed in the jobTimeScheduler CRD
    bestStartTimeString = doBestTimeEstimation(cronJobtimescheduler)

    #the API returns besttime in UTC
    bestStartTime = pd.Timestamp(bestStartTimeString, tz='UTC')

    #Create corresponding CronJobExpression, by updating only hour and minute in expression
    newcronexpression = "%s %s * * * " % (bestStartTime.minute, bestStartTime.hour)


    # Schedule Time:Hour for Job + add annotation for bestStartTime
    cronjob_patch = { 
                'spec' : {'schedule': newcronexpression } ,
                'metadata' : {'annotations' : {
                    'bestStartTime' : bestStartTimeString
                        } }
                    }
    api = kubernetes.client.BatchV1Api()
    obj = api.patch_namespaced_cron_job(name, namespace, cronjob_patch)
    print("Scheduled next occurence of newly created CronJob %s at bestTime found (tz=UTC) : %s" % (name,bestStartTime))

##############################


#Manage CronJob next job scheduling 
@kopf.timer('cronjobs', annotations={'bestStartTime': kopf.PRESENT}, interval=8.0) 
def TimeSchedulebNextJobOccurence(body, spec, name, namespace, status, labels, annotations, **kwargs):


    scheduledTimeString = annotations["bestStartTime"]
    nextScheduledJobTime = pd.Timestamp(scheduledTimeString, tz='UTC')

    if not("lastScheduleTime" in status.keys()) :
        print("First execution of Cronjob/Job %s did not happen yet. Planned at :  %s" % (name,scheduledTimeString)) 
        return    #first run did not happen yet 


    lastExecutedJobTimeStatus = status["lastScheduleTime"]
    lastExecutedJobTime = pd.Timestamp(lastExecutedJobTimeStatus).tz_convert('UTC')

    if lastExecutedJobTime < nextScheduledJobTime: # the Planned / scheduled Job did not execute yet 
        # Next occurence of Job did not execute yet, do nothing
        print("CronJob %s => lastExecutedJobAt(UTC): %s ; nextScheduledJobAt(UTC) : %s => nothing to do" % (name,lastExecutedJobTime, nextScheduledJobTime))

    else:
        print("CronJob %s => lastExecutedJobAt: %s  => finding NextBestTime for next Job occurence." % (name,lastExecutedJobTime))
        # find nextbestTime to schedule next Job occurence, in the next 24h

        # find Matching cronJobTimeScheduler for current Job
        cronJobtimescheduler = findMatchingCronJobTimeScheduler(namespace, labels) 
        if cronJobtimescheduler is None : return # No TimeScheduler found, do nothing
        

        bestStartTimeString = doBestTimeEstimation(cronJobtimescheduler)

        bestStartTime = pd.Timestamp(bestStartTimeString, tz='UTC')

        if bestStartTime <= lastExecutedJobTime:
            print("CronJob %s => lastExecutedJobAt: %s ; nextProposedBestTime : %s is outdated => waiting for updated forecast" % (name,lastExecutedJobTime, nextScheduledJobTime))
            # do nothing
            return
        

        #Create corresponding CronJobExpression, by updating only hour and minute in expression
        newcronexpression = "%s %s * * * " % (bestStartTime.minute, bestStartTime.hour)


        # Schedule Time:Hour for Job + add annotation for bestStartTime
        cronjob_patch = { 
                    'spec' : {'schedule': newcronexpression } ,
                    'metadata' : {'annotations' : {
                        'bestStartTime' : bestStartTimeString
                            } }
                        }
        api = kubernetes.client.BatchV1Api()
        obj = api.patch_namespaced_cron_job(name, namespace, cronjob_patch)
        print("Scheduled next occurence of CronJob %s at bestTime Found (tz=UTC) %s" % (name,bestStartTime))

##############################
