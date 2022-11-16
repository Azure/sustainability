---
sidebar_position: 3
---

# AKS - Time Shift CronJobs

## Description
The carbon emissions of a software system depends on the power consumed by that software, but also on the Carbon intensity of the electricity it is powered on. For this reason, running energy-efficient software on carbon intensive electricity grid, might be inefficient to reduce its global carbon emissions.

Carbon aware time scheduling, is about scheduling workloads to execute, when electricity carbon intensity is low.

## Solution

Kubernetes recurrent Jobs (such as ML Training Jobs, Batchs, etc.) are implemented as CronJobs. They can be time shifted by using carbon intensity Forecast data (24h usually, depdening on the Electricity data provider), to calculate the best time in the future to execute the job.

## SCI Impact

SCI = (E * I) + M per R [Software Carbon Intensity Spec](https://github.com/Green-Software-Foundation/software_carbon_intensity/blob/main/Software_Carbon_Intensity/Software_Carbon_Intensity_Specification.md)

Regarding the SCI equation, Time shifting will impact:

I: The goal is to reduce SCI by reducing carbon intensity.

## Demo
