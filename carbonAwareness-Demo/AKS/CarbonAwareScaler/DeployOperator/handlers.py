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
    return getCarbonIntensityFromProm()
##############################


def get_existing_scaledObject(scaledObjectsList, name):     
    for scaledObject in scaledObjectsList["items"]:
        scaledObjectName = scaledObject['metadata']['name']
        if scaledObjectName == name:
            return scaledObject
    return None


def patch_namespaced_scaledObject(api, namespace, scaledObject, patch_data):
    obj = api.patch_namespaced_custom_object(
        group="keda.sh",
        version="v1alpha1",
        name="httpj",
        namespace="default",
        plural="scaledobjects",
        body=patch_data,
    )     
    return obj

def list_scaledObjects_in_namespace(api, namespace):
    scaledObjects = api.list_namespaced_custom_object(
        group="keda.sh",
        version="v1alpha1",
        namespace="default",
        plural="scaledobjects",
    )     
    return scaledObjects

def list_carbonAwareScalers_in_namespace(api, namespace):
    #carbonAwareScalersList = api.list_namespaced_custom_object(
    carbonAwareScalersList = api.list_cluster_custom_object(
        group="carbon-aware-actions.kubernetes",
        version="dev",
        #namespace="default",
        plural="carbonawarescalers",
    )     
    return carbonAwareScalersList

def get_existing_carbonAwareScaler(carbonAwareScalersList, name):     
    for carbonawarescaler in carbonAwareScalersList["items"]:
        targetScaledObjectName = carbonawarescaler['spec']['kedaScaledObjectRef']['name']
        if targetScaledObjectName == name:
            return carbonawarescaler
    return None


##############################


"""
@kopf.on.event('scaledobjects')
def my_handler(event, **_):
   
    print(event)
"""

##############################


#Carbon Aware scaling
@kopf.timer('carbonawarescalers.carbon-aware-actions.kubernetes', interval=5.0) 
def carbonAwareKeda(body, spec, name, namespace, status, annotations, **kwargs):


    keda_scaledObjectName = spec['kedaScaledObjectRef']['name']
    defaultMaxReplicaCount = spec['defaultMaxReplicaCount']

    scalingRules = spec['scalingRules']
    sortedScalingRules = sorted(scalingRules, key=lambda k: k['carbonIntensity']) 

    carbonIntensityValues = [ rule["carbonIntensity"] for rule in sortedScalingRules]
    allowedMaxReplicaCountValues = [ rule["allowedMaxReplicaCount"] for rule in sortedScalingRules]

    
    carbon_rating = getCarbonIntensity()
    if carbon_rating is None: 
        return

    if carbon_rating < min(carbonIntensityValues): #use orginalMaxReplicaCount as it is the highest value
        maxReplicaTarget = int(defaultMaxReplicaCount)

    elif carbon_rating >= max(carbonIntensityValues): #use smallest value
        maxReplicaTarget = allowedMaxReplicaCountValues[-1]

    else: #Use closest value for current carbonIntensity
        i=0
        while (carbon_rating > carbonIntensityValues[i]) : i=i+1
        maxReplicaTarget = allowedMaxReplicaCountValues[i-1] # list starts with O

    keda_scaledobject_patch = {'spec': {'maxReplicaCount': maxReplicaTarget}}

    api = kubernetes.client.CustomObjectsApi()
    obj = patch_namespaced_scaledObject(api, namespace, keda_scaledObjectName, keda_scaledobject_patch)

    eventReason = "CarbonAwareScaling"
    eventMessage = "Setting maxReplicaCount to {}".format(maxReplicaTarget)
    kopf.info(body, reason=eventReason, message=eventMessage)

