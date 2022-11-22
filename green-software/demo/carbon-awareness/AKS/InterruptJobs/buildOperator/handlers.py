import os
import kopf
import kubernetes
import yaml
import asyncio
import time
import requests
import json



CARBON_INTENSITY_API_URL = os.getenv("CARBON_INTENSITY_API_URL", default="https://og-serverless.azure-api.net/electricitymaphack/getCarbonIntensityLatest")


ELECTRICITYMAP_ZONE = os.getenv("ELECTRICITYMAP_ZONE", default="FR")

def getCarbonIntensityFromHackathonAPI():
    response = requests.get("%s?zone=%s" % (CARBON_INTENSITY_API_URL, ELECTRICITYMAP_ZONE))
    json_data = response.json() if response and response.status_code == 200 else None
    carbon_rating = json_data['carbonIntensity'] if json_data and 'carbonIntensity' in json_data else None
    return carbon_rating 

def getCarbonIntensityFromCarbonRating():
    response = requests.get('https://greenapimockyaya.azurewebsites.net/api/CarbonRating')
    json_data = response.json() if response and response.status_code == 200 else None
    carbon_rating = json_data['Rating'] if json_data and 'Rating' in json_data else None
    return carbon_rating 

def getCarbonIntensity():
    return getCarbonIntensityFromHackathonAPI()
##############################


#Interrupt Jobs when Carbon Intensity is High
@kopf.timer('JobInterruptor.carbon-aware-actions.kubernetes', interval=5.0) 
def interruptJobs(body, spec, name, namespace, status, annotations, **kwargs):


    jobName = spec["jobRef"]["name"]
    if jobName == "" or jobName is None : return 

    jobNamespace = "default"

    carbonIntensityThreshold = spec.get("pauseJobWhenCarbonIntensityAbove", -1)
    if carbonIntensityThreshold < 0 : return

    current_CarbonIntensity = getCarbonIntensity()

    if current_CarbonIntensity >= carbonIntensityThreshold : 
        job_patch = {'spec': {'suspend': True}}
        print("Processing Job :%s ;  current carbonIntensity is %s  ; jobCarbonIntensityThreshold is %s => suspending Job" % (jobName, current_CarbonIntensity, carbonIntensityThreshold))
    else: 
        job_patch = {'spec': {'suspend': False}}
        print("Processing Job : %s, current carbonIntensity is %s  ; jobCarbonIntensityThreshold is %s => resuming Job" % (jobName, current_CarbonIntensity, carbonIntensityThreshold))

    api = kubernetes.client.BatchV1Api()
    obj = api.patch_namespaced_job(jobName, jobNamespace, job_patch)

    

##############################
