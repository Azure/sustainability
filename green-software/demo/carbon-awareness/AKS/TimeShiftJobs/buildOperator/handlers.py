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
##############################


# utility func
def findMatchingJobTimeScheduler(jobnamespace, joblabels):

    api = kubernetes.client.CustomObjectsApi()
    jobTimeSchedulersList = api.list_namespaced_custom_object(
        group="carbon-aware-actions.kubernetes",
        version="dev",
        namespace=jobnamespace,
        plural="jobtimeschedulers",
    )     

    for jobtimescheduler in jobTimeSchedulersList["items"]:
        targetJobLabels = jobtimescheduler["spec"]["jobRef"]["labels"]
        for key in joblabels:
            if ((key in targetJobLabels) and (joblabels[key] == targetJobLabels[key])):  #if job labels match as a taget for JobTimeScheduler Operator
                return jobtimescheduler
    
    return None


##############################
#When Job is created/updated, suspend Job and findBestTime in the future to schedule the Job
@kopf.on.create('jobs') 
def SuspendAndScheduleJob(body, spec, name, namespace, status, annotations, labels, **kwargs):


    # find Matching jobTimeScheduler for current Job
    jobtimescheduler = findMatchingJobTimeScheduler(namespace, labels) 
    if jobtimescheduler is None : return # No TimeScheduler found, do nothing
    
    jobDuration = jobtimescheduler["spec"]["jobDuration"]
    location = jobtimescheduler["spec"]["location"]

    jobDeadline_hour_minute = jobtimescheduler["spec"]["jobDeadline"]
    #figure out the day corresponding to the deadline: today or tomorrow

    currentTime = pd.Timestamp.now()
    currentTime_string = currentTime.strftime('%Y-%m-%d %X')

    jobDeadline = pd.Timestamp(jobDeadline_hour_minute)
    
    
    if currentTime >= jobDeadline : jobDeadline = jobDeadline + pd.Timedelta(days=1)  #if deadline is 09:00; and current time is 20:00 => job deadline is in the following day

    jobDeadline_string = jobDeadline.strftime('%Y-%m-%d %X')

    # find Best time to schedule job, based on the constraints expressed in the jobTimeScheduler CRD
    bestStartTime = findBestContinuousTimeSlot(currentTime_string, jobDeadline_string, jobDuration, location)

    # Suspend Job + add annotation for bestStartTime
    job_patch = {'spec': {'suspend': True},
                'metadata' : {'annotations' : {
                    'bestStartTime' : bestStartTime
                    } }
                }
    api = kubernetes.client.BatchV1Api()
    obj = api.patch_namespaced_job(name, namespace, job_patch)
    print("Suspending newly created Job %s to be scheduled at bestTime with lowest Carbon Intensity at %s" % (name,bestStartTime))

##############################


#Resume / Unsuspend Job when it is time to run it 
@kopf.timer('jobs', annotations={'bestStartTime': kopf.PRESENT}, field='spec.suspend', value=True, interval=5.0) 
def interruptJobs(body, spec, name, namespace, status, annotations, **kwargs):

    scheduledTimeString = annotations["bestStartTime"]
    scheduledTime = pd.Timestamp(scheduledTimeString)

    currentTime = pd.Timestamp.now()

    if currentTime > scheduledTime :
        print("Current time is %s .Reached Scheduling Time for Job %s, planned to run at %s => Running Job Now" % (currentTime, name, scheduledTime))

        job_patch = {'spec': {'suspend': True},
                'metadata' : {'annotations' : {
                    'bestStartTime' : None
                    } }
                }
        api = kubernetes.client.BatchV1Api()
        obj = api.patch_namespaced_job(name, namespace, job_patch)

    else:
        print("Current time is %s .Still has not reached Scheduling Time for Job %s, planned to run at %s => Nothing to do." % (currentTime, name, scheduledTime))
    

##############################
