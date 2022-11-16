import logging

import azure.functions as func

import pandas as pd

import json

data = {
    "zone": "FR",
    "forecast": [
        {
            "carbonIntensity": 85,
            "datetime": "2022-11-13T20:00:00.000Z"
        },
        {
            "carbonIntensity": 86,
            "datetime": "2022-11-13T21:00:00.000Z"
        },
        {
            "carbonIntensity": 87,
            "datetime": "2022-11-13T22:00:00.000Z"
        },
        {
            "carbonIntensity": 84,
            "datetime": "2022-11-13T23:00:00.000Z"
        },
        {
            "carbonIntensity": 92,
            "datetime": "2022-11-14T00:00:00.000Z"
        },
        {
            "carbonIntensity": 92,
            "datetime": "2022-11-14T01:00:00.000Z"
        },
        {
            "carbonIntensity": 90,
            "datetime": "2022-11-14T02:00:00.000Z"
        },
        {
            "carbonIntensity": 88,
            "datetime": "2022-11-14T03:00:00.000Z"
        },
        {
            "carbonIntensity": 88,
            "datetime": "2022-11-14T04:00:00.000Z"
        },
        {
            "carbonIntensity": 91,
            "datetime": "2022-11-14T05:00:00.000Z"
        },
        {
            "carbonIntensity": 96,
            "datetime": "2022-11-14T06:00:00.000Z"
        },
        {
            "carbonIntensity": 99,
            "datetime": "2022-11-14T07:00:00.000Z"
        },
        {
            "carbonIntensity": 101,
            "datetime": "2022-11-14T08:00:00.000Z"
        },
        {
            "carbonIntensity": 97,
            "datetime": "2022-11-14T09:00:00.000Z"
        },
        {
            "carbonIntensity": 97,
            "datetime": "2022-11-14T10:00:00.000Z"
        },
        {
            "carbonIntensity": 96,
            "datetime": "2022-11-14T11:00:00.000Z"
        },
        {
            "carbonIntensity": 92,
            "datetime": "2022-11-14T12:00:00.000Z"
        },
        {
            "carbonIntensity": 90,
            "datetime": "2022-11-14T13:00:00.000Z"
        },
        {
            "carbonIntensity": 93,
            "datetime": "2022-11-14T14:00:00.000Z"
        },
        {
            "carbonIntensity": 93,
            "datetime": "2022-11-14T15:00:00.000Z"
        },
        {
            "carbonIntensity": 96,
            "datetime": "2022-11-14T16:00:00.000Z"
        },
        {
            "carbonIntensity": 99,
            "datetime": "2022-11-14T17:00:00.000Z"
        },
        {
            "carbonIntensity": 104,
            "datetime": "2022-11-14T18:00:00.000Z"
        },
        {
            "carbonIntensity": 105,
            "datetime": "2022-11-14T19:00:00.000Z"
        },
        {
            "carbonIntensity": 85,
            "datetime": "2022-11-14T20:00:00.000Z"
        },
        {
            "carbonIntensity": 86,
            "datetime": "2022-11-14T21:00:00.000Z"
        },
        {
            "carbonIntensity": 87,
            "datetime": "2022-11-14T22:00:00.000Z"
        },
        {
            "carbonIntensity": 84,
            "datetime": "2022-11-14T23:00:00.000Z"
        },
        {
            "carbonIntensity": 92,
            "datetime": "2022-11-15T00:00:00.000Z"
        },
        {
            "carbonIntensity": 92,
            "datetime": "2022-11-15T01:00:00.000Z"
        },
        {
            "carbonIntensity": 90,
            "datetime": "2022-11-15T02:00:00.000Z"
        },
        {
            "carbonIntensity": 88,
            "datetime": "2022-11-15T03:00:00.000Z"
        },
        {
            "carbonIntensity": 88,
            "datetime": "2022-11-15T04:00:00.000Z"
        },
        {
            "carbonIntensity": 91,
            "datetime": "2022-11-15T05:00:00.000Z"
        },
        {
            "carbonIntensity": 96,
            "datetime": "2022-11-15T06:00:00.000Z"
        },
        {
            "carbonIntensity": 99,
            "datetime": "2022-11-15T07:00:00.000Z"
        },
        {
            "carbonIntensity": 101,
            "datetime": "2022-11-15T08:00:00.000Z"
        },
        {
            "carbonIntensity": 97,
            "datetime": "2022-11-15T09:00:00.000Z"
        },
        {
            "carbonIntensity": 97,
            "datetime": "2022-11-15T10:00:00.000Z"
        },
        {
            "carbonIntensity": 96,
            "datetime": "2022-11-15T11:00:00.000Z"
        },
        {
            "carbonIntensity": 92,
            "datetime": "2022-11-15T12:00:00.000Z"
        },
        {
            "carbonIntensity": 90,
            "datetime": "2022-11-15T13:00:00.000Z"
        },
        {
            "carbonIntensity": 93,
            "datetime": "2022-11-15T14:00:00.000Z"
        },
        {
            "carbonIntensity": 93,
            "datetime": "2022-11-15T15:00:00.000Z"
        },
        {
            "carbonIntensity": 96,
            "datetime": "2022-11-15T16:00:00.000Z"
        },
        {
            "carbonIntensity": 99,
            "datetime": "2022-11-15T17:00:00.000Z"
        },
        {
            "carbonIntensity": 104,
            "datetime": "2022-11-15T18:00:00.000Z"
        },
        {
            "carbonIntensity": 105,
            "datetime": "2022-11-15T19:00:00.000Z"
        }
    ],
    "updatedAt": "2022-11-13T19:51:31.548Z"
}



#print(df.between_time("00:00", "07:00"))

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Starting Function')

    #jobDuration = req.params.get('jobDuration')
    #jobDeadline = req.params.get('jobDeadline')



    paramjobDuration  = req.params.get("jobDuration")
    paramjobDeadline  = req.params.get("jobDeadline")
    zone  = req.params.get("zone") #zone is region in ElectricityMap jargon

    jobDuration = int(paramjobDuration)
    jobDeadlineString = paramjobDeadline
    
    jobDeadline = pd.Timestamp(paramjobDeadline)
    jobEarliestStart = pd.Timestamp.now() 
    #jobEarliestStartString = "{}:{}".format(jobEarliestStartDate.hour, jobEarliestStartDate.minute) 
    

    df=pd.json_normalize(data.get("forecast", []))


    #set endTime column as a timeIndex for the DataFrame
    df['endTime'] = pd.DatetimeIndex(df['datetime'])

    df = df.set_index(df['endTime'])

    #compute rolling averages for carbon intensity, for time Window equal to Job duration
    df['carbonIntensityRollingAverage'] = df['carbonIntensity'].rolling(jobDuration).mean()


    print("\ncalculating carbon Intensity rolling averages, for window size of job duration = {}hours \n".format(jobDuration))
    print(df)

    # filter dates before job deadline

    jobEarliestEnd = jobEarliestStart + pd.Timedelta(hours=jobDuration)

    #since data is hourly, we need to decide whether to include the data row corresponding to the current hour in the estimation, or to start from the next hour 
    # we decide based on time.minutes : if past half hour or not
    minutes_offset = 0 if jobEarliestEnd.minute <= 30  else jobEarliestEnd.minute
   
    jobEarliestEndString = "{}:{}".format(jobEarliestEnd.hour, minutes_offset) 

    # slice rows and keep the slots between earliest end and deadline (since the df timeIndex is EndTime)
    # since data is hourly:
    # if jobEarliestEndString = 18:23 ; df starts from the next slot 19:00
    # if jobEarliestEndString = 18:00 ; df starts from current slot 18:00 => c.f why using minutes_offset above
    df = df.between_time(jobEarliestEndString, jobDeadlineString)  #returns time slices based on hour, for several days, needs to filter days below


    # figure out which day corresponds to deadline : current or next day
    deadline_hour = jobDeadline.hour
    jobEarliestStart_hour = jobEarliestStart.hour

    deadline_day = -1
    if deadline_hour <= jobEarliestStart_hour:
        deadline_day = jobEarliestStart.day + 1 # next day
    else:
        deadline_day = jobEarliestStart.day # current day

    if deadline_day < 0 : return

    # the dataset contains forecast for several days depending on the provider, we keep only the closest day (day of deadline)
    df = df[ (df["endTime"].dt.day ) == deadline_day ]

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
        "bestStartTime" : jobEarliestStart.strftime('%Y-%m-%d %X'),
        "earliestStartTime": jobEarliestStart.strftime('%Y-%m-%d %X'),
        "averagecarbonSavings" : 0,
        "timeshiftstatus" : "JobLateForDeadline"

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

    response = {
        "bestStartTime" : bestslot["startTime"].strftime('%Y-%m-%d %X'),
        "earliestStartTime": earliestslot["startTime"].strftime('%Y-%m-%d %X'),
        "averagecarbonSavings" : averagecarbonSavings,
        "timeshiftstatus" : "foundBestTimeforSchedulingJob"
    }
    return json.dumps(response)
