import logging

import azure.functions as func

import pandas as pd

import json

data = {
    "zone": "FR",
    "forecast": [
        {
            "carbonIntensity": 110,
            "datetime": "2022-11-26T08:00:00.000Z"
        },
        {
            "carbonIntensity": 107,
            "datetime": "2022-11-26T09:00:00.000Z"
        },
        {
            "carbonIntensity": 101,
            "datetime": "2022-11-26T10:00:00.000Z"
        },
        {
            "carbonIntensity": 95,
            "datetime": "2022-11-26T11:00:00.000Z"
        },
        {
            "carbonIntensity": 88,
            "datetime": "2022-11-26T12:00:00.000Z"
        },
        {
            "carbonIntensity": 90,
            "datetime": "2022-11-26T13:00:00.000Z"
        },
        {
            "carbonIntensity": 91,
            "datetime": "2022-11-26T14:00:00.000Z"
        },
        {
            "carbonIntensity": 91,
            "datetime": "2022-11-26T15:00:00.000Z"
        },
        {
            "carbonIntensity": 100,
            "datetime": "2022-11-26T16:00:00.000Z"
        },
        {
            "carbonIntensity": 110,
            "datetime": "2022-11-26T17:00:00.000Z"
        },
        {
            "carbonIntensity": 113,
            "datetime": "2022-11-26T18:00:00.000Z"
        },
        {
            "carbonIntensity": 112,
            "datetime": "2022-11-26T19:00:00.000Z"
        },
        {
            "carbonIntensity": 109,
            "datetime": "2022-11-26T20:00:00.000Z"
        },
        {
            "carbonIntensity": 110,
            "datetime": "2022-11-26T21:00:00.000Z"
        },
        {
            "carbonIntensity": 110,
            "datetime": "2022-11-26T22:00:00.000Z"
        },
        {
            "carbonIntensity": 100,
            "datetime": "2022-11-26T23:00:00.000Z"
        },
        {
            "carbonIntensity": 98,
            "datetime": "2022-11-27T00:00:00.000Z"
        },
        {
            "carbonIntensity": 97,
            "datetime": "2022-11-27T01:00:00.000Z"
        },
        {
            "carbonIntensity": 92,
            "datetime": "2022-11-27T02:00:00.000Z"
        },
        {
            "carbonIntensity": 88,
            "datetime": "2022-11-27T03:00:00.000Z"
        },
        {
            "carbonIntensity": 91,
            "datetime": "2022-11-27T04:00:00.000Z"
        },
        {
            "carbonIntensity": 94,
            "datetime": "2022-11-27T05:00:00.000Z"
        },
        {
            "carbonIntensity": 97,
            "datetime": "2022-11-27T06:00:00.000Z"
        },
        {
            "carbonIntensity": 98,
            "datetime": "2022-11-27T07:00:00.000Z"
        },
        {
            "carbonIntensity": 110,
            "datetime": "2022-11-27T08:00:00.000Z"
        },
        {
            "carbonIntensity": 107,
            "datetime": "2022-11-27T09:00:00.000Z"
        },
        {
            "carbonIntensity": 101,
            "datetime": "2022-11-27T10:00:00.000Z"
        },
        {
            "carbonIntensity": 95,
            "datetime": "2022-11-27T11:00:00.000Z"
        },
        {
            "carbonIntensity": 88,
            "datetime": "2022-11-27T12:00:00.000Z"
        },
        {
            "carbonIntensity": 90,
            "datetime": "2022-11-27T13:00:00.000Z"
        },
        {
            "carbonIntensity": 91,
            "datetime": "2022-11-27T14:00:00.000Z"
        },
        {
            "carbonIntensity": 91,
            "datetime": "2022-11-27T15:00:00.000Z"
        },
        {
            "carbonIntensity": 100,
            "datetime": "2022-11-27T16:00:00.000Z"
        },
        {
            "carbonIntensity": 110,
            "datetime": "2022-11-27T17:00:00.000Z"
        },
        {
            "carbonIntensity": 113,
            "datetime": "2022-11-27T18:00:00.000Z"
        },
        {
            "carbonIntensity": 112,
            "datetime": "2022-11-27T19:00:00.000Z"
        },
        {
            "carbonIntensity": 109,
            "datetime": "2022-11-27T20:00:00.000Z"
        },
        {
            "carbonIntensity": 110,
            "datetime": "2022-11-27T21:00:00.000Z"
        },
        {
            "carbonIntensity": 110,
            "datetime": "2022-11-27T22:00:00.000Z"
        },
        {
            "carbonIntensity": 100,
            "datetime": "2022-11-27T23:00:00.000Z"
        },
        {
            "carbonIntensity": 98,
            "datetime": "2022-11-28T00:00:00.000Z"
        },
        {
            "carbonIntensity": 97,
            "datetime": "2022-11-28T01:00:00.000Z"
        },
        {
            "carbonIntensity": 92,
            "datetime": "2022-11-28T02:00:00.000Z"
        },
        {
            "carbonIntensity": 88,
            "datetime": "2022-11-28T03:00:00.000Z"
        },
        {
            "carbonIntensity": 91,
            "datetime": "2022-11-28T04:00:00.000Z"
        },
        {
            "carbonIntensity": 94,
            "datetime": "2022-11-28T05:00:00.000Z"
        },
        {
            "carbonIntensity": 97,
            "datetime": "2022-11-28T06:00:00.000Z"
        },
        {
            "carbonIntensity": 98,
            "datetime": "2022-11-28T07:00:00.000Z"
        }
    ],
    "updatedAt": "2022-11-26T07:51:29.195Z"
}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Starting Function')


    paramjobDuration  = req.params.get("jobDuration")
    paramjobDeadline  = req.params.get("jobDeadline")
    paramjobEarliestStart  = req.params.get("jobEarliestStart")
    paramZone  = req.params.get("zone") #zone is region in ElectricityMap jargon

    if (paramjobDuration is None) or (paramjobDeadline is None) or (paramjobEarliestStart is None) or (paramZone is None):
        print("missing required params : jobDuration, jobEarliestStart, jobDeadline, zone ")
        return func.HttpResponse(
             "missing required params : jobDuration, jobEarliestStart, jobDeadline, zone ",
             status_code=400
        )

    jobDuration = int(paramjobDuration)
    
    jobDeadline = pd.Timestamp(paramjobDeadline, tz='UTC')
    jobDeadline_in_hour_minutes = "{}:{}".format(jobDeadline.hour, jobDeadline.minute) 

    jobEarliestStart = pd.Timestamp(paramjobEarliestStart, tz='UTC') 


    # First check if scheduling Job with time constraints is possible

    jobEarliestEnd = jobEarliestStart + pd.Timedelta(hours=jobDuration)


    #before proceeding further, check if job can be scheduled in the future, or is past deadline
    if jobEarliestEnd > jobDeadline:
        print("Job is late for deadline, schedule to run now")
        
        response = {
        "bestStartTime" : jobEarliestStart.isoformat(),
        "earliestStartTime": jobEarliestStart.isoformat(),
        "averagecarbonSavings" : 0,
        "timeshiftstatus" : "JobLateForDeadline"

        }
        return json.dumps(response)



    # Fetch the latest Forecast Data
    df=pd.json_normalize(data.get("forecast", []))


    #Filter Data Frame based on time, between Job EarliestStart and Deadline
    df['datetime'] = pd.DatetimeIndex(df['datetime'])

    df = df.set_index(df['datetime'])



    filtering_condition = df.index.to_series().between(paramjobEarliestStart, paramjobDeadline)
    df = df[ filtering_condition ]



   #For caculating rolling averages, we'll set endTime (of the job) as a timeIndex for the DataFrame
    df['endTime'] = pd.DatetimeIndex(df['datetime'])

    df = df.set_index(df['endTime'])


    #compute rolling averages for carbon intensity, for time Window equal to Job duration
    df['carbonIntensityRollingAverage'] = df['carbonIntensity'].rolling(jobDuration).mean()


    print("\ncalculating carbon Intensity rolling averages, for window size of job duration = {}hours \n".format(jobDuration))
    print(df)




    #since data is hourly, we need to decide whether to include the data row corresponding to the current hour in the estimation, or to start from the next hour 
    # we decide based on time.minutes : if past half hour or not
    minutes_offset = 0 if jobEarliestEnd.minute <= 30  else jobEarliestEnd.minute
   
    jobEarliestEnd_in_hour_minutes = "{}:{}".format(jobEarliestEnd.hour, minutes_offset) 

    # slice rows and keep the slots between earliest end and deadline (since the df timeIndex is EndTime)
    # since data is hourly:
    # if jobEarliestEnd_in_hour_minutes = 18:23 ; df starts from the next slot 19:00
    # if jobEarliestEnd_in_hour_minutes = 18:00 ; df starts from current slot 18:00 => c.f why using minutes_offset above
    df = df.between_time(jobEarliestEnd_in_hour_minutes, jobDeadline_in_hour_minutes)  #returns time slices based on hour, for several days, needs to filter days below


    # figure out which day corresponds to deadline : current or next day
    #deadline_hour = jobDeadline.hour
    #jobEarliestStart_hour = jobEarliestStart.hour

    #deadline_day = -1
    #if deadline_hour <= jobEarliestStart_hour:
     #   deadline_day = jobEarliestStart.day + 1 # next day
    #else:
    #    deadline_day = jobEarliestStart.day # current day

    #if deadline_day < 0 : return

    # the dataset contains forecast for several days depending on the provider, we keep only the closest day (day of deadline)
    #df = df[ (df["endTime"].dt.day ) == deadline_day ]

    # prepapre response: add column job startTime based on endTime - jobDuration
    df['startTime'] = pd.DatetimeIndex(df['endTime']) - pd.Timedelta(hours=jobDuration)
    df = df[df.columns[df.columns.isin(['startTime', 'carbonIntensityRollingAverage', 'endTime'])]]

    print("\nSlicing Time slots between Job Earliest End (EarliestStart + Duration) and Job deadline\n")
    print(df)

    # if sliced data frame is empty, meaning no slot was found that respects deadline
    # run now / use earliest slot 
    if df.empty:
        print("no Time Slot found that respects deadline ; schedule for running now")
        print(jobEarliestStart)
        
        response = {
        "bestStartTime" : jobEarliestStart.isoformat(),
        "earliestStartTime": jobEarliestStart.isoformat(),
        "averagecarbonSavings" : 0,
        "timeshiftstatus" : "CouldNotFindBestTimeSlot"

        }
        return json.dumps(response)



    #Get index of minimal value for carbonIntensityRollingAverage
    minidx = df["carbonIntensityRollingAverage"].idxmin()

    print("\nBest Found Slot\n")
    bestslot = df.loc[minidx]
    print(bestslot)

    print("\n\n")

    print("\n carbonIntensityRollingAverage for running Job at Earliest time Slot\n")
    earliestslot = df.iloc[0]
    print(earliestslot)

    print("\n\n")

    averagecarbonSavings = earliestslot["carbonIntensityRollingAverage"] - bestslot["carbonIntensityRollingAverage"]

    print("\n Estimated Carbon Savings, based on CarbonIntensityRollingAverage \n")
    print("saved around %s CO2eq/KHW by Time Shifting the Job" % (averagecarbonSavings) )

    if jobEarliestStart > bestslot["startTime"]:
        #if earliest start time = 18:23 and the best time slot is the earliest => bestSlot would be 18:00 => so we return the earliest start date in this case
        response = {
            "bestStartTime" : paramjobEarliestStart,
                        "bestStartTimeCarbonItensity" : bestslot["carbonIntensityRollingAverage"],
            "earliestStartTime": paramjobEarliestStart,
                       "earliestStartTimeCarbonIntensity": earliestslot["carbonIntensityRollingAverage"],
            "averagecarbonSavings" : averagecarbonSavings,
            "timeshiftstatus" : "foundBestTimeforSchedulingJob"
        }
    
    else:
        print(bestslot["startTime"].isoformat())
        response = {
        "bestStartTime" : bestslot["startTime"].isoformat(),
                                "bestStartTimeCarbonItensity" : bestslot["carbonIntensityRollingAverage"],

        "earliestStartTime": earliestslot["startTime"].isoformat(),
                               "earliestStartTimeCarbonIntensity": earliestslot["carbonIntensityRollingAverage"],

        "averagecarbonSavings" : averagecarbonSavings,
        "timeshiftstatus" : "foundBestTimeforSchedulingJob"
        }   
    return json.dumps(response)
