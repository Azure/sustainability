import os
import kopf
import kubernetes
import yaml
import asyncio
import time
import requests
import json

#prom_endpoint = os.getenv("PROM_ENDPOINT", default="https://prometheus.carbon-intensity-exporter.svc.cluster.local:9090")

prom_endpoint = os.getenv("PROM_ENDPOINT", default="http://20.250.74.89:9090")
prom_query = os.getenv("PROM_QUERY", default="carbon_intensity")

def getCarbonIntensityFromProm():


    params={
        'query': prom_query
    }
    response = requests.get(prom_endpoint+'/api/v1/query', params=params)
    results = response.json()['data']['result']
    if len(results) > 0:
        carbon_intensity_value = results[0]['value'][1]
        print("current carbon intensity (CO2eq/KWH) : " + carbon_intensity_value)
        return int(carbon_intensity_value)
    return None



def getCarbonIntensityFromCarbonRating():
    response = requests.get('https://greenapimockyaya.azurewebsites.net/api/CarbonRating')
    json_data = response.json() if response and response.status_code == 200 else None
    carbon_rating = json_data['Rating'] if json_data and 'Rating' in json_data else None
    return carbon_rating 

def getCarbonIntensity():
    #return getCarbonIntensityFromCarbonRating()
    #return getCarbonIntensityFromProm()
    return 200
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
