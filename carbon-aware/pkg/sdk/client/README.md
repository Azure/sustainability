# Go API client for Carbon Aware Sustainability

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

## Overview
This API client was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project.  By using the [swagger-spec](https://github.com/swagger-api/swagger-spec) from a remote server, you can easily generate an API client.

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.go.GoClientCodegen

## Installation
Put the package under your project folder and add the following in import:
```golang
import "./client"
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/Microsoft-hela/carbonaware/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CarbonAwareApi* | [**BatchForecastDataAsync**](docs/CarbonAwareApi.md#batchforecastdataasync) | **Post** /emissions/forecasts/batch | Given an array of historical forecasts, retrieves the data that contains  forecasts metadata, the optimal forecast and a range of forecasts filtered by the attributes [start...end] if provided.
*CarbonAwareApi* | [**GetAverageCarbonIntensity**](docs/CarbonAwareApi.md#getaveragecarbonintensity) | **Get** /emissions/average-carbon-intensity | Retrieves the measured carbon intensity data between the time boundaries and calculates the average carbon intensity during that period.
*CarbonAwareApi* | [**GetAverageCarbonIntensityBatch**](docs/CarbonAwareApi.md#getaveragecarbonintensitybatch) | **Post** /emissions/average-carbon-intensity/batch | Given an array of request objects, each with their own location and time boundaries, calculate the average carbon intensity for that location and time period   and return an array of carbon intensity objects.
*CarbonAwareApi* | [**GetBestEmissionsDataForLocationsByTime**](docs/CarbonAwareApi.md#getbestemissionsdataforlocationsbytime) | **Get** /emissions/bylocations/best | Calculate the best emission data by list of locations for a specified time period.
*CarbonAwareApi* | [**GetCurrentForecastData**](docs/CarbonAwareApi.md#getcurrentforecastdata) | **Get** /emissions/forecasts/current | Retrieves the most recent forecasted data and calculates the optimal marginal carbon intensity window.
*CarbonAwareApi* | [**GetEmissionsDataForLocationByTime**](docs/CarbonAwareApi.md#getemissionsdataforlocationbytime) | **Get** /emissions/bylocation | Calculate the best emission data by location for a specified time period.
*CarbonAwareApi* | [**GetEmissionsDataForLocationsByTime**](docs/CarbonAwareApi.md#getemissionsdataforlocationsbytime) | **Get** /emissions/bylocations | Calculate the observed emission data by list of locations for a specified time period.
*LocationsApi* | [**GetAllLocations**](docs/LocationsApi.md#getalllocations) | **Get** /locations | Get all locations instances

## Documentation For Models

 - [CarbonIntensityBatchParametersDto](docs/CarbonIntensityBatchParametersDto.md)
 - [CarbonIntensityDto](docs/CarbonIntensityDto.md)
 - [EmissionsData](docs/EmissionsData.md)
 - [EmissionsDataDto](docs/EmissionsDataDto.md)
 - [EmissionsForecastBatchParametersDto](docs/EmissionsForecastBatchParametersDto.md)
 - [EmissionsForecastDto](docs/EmissionsForecastDto.md)
 - [Location](docs/Location.md)

## Documentation For Authorization

 Endpoints do not require authorization.

## Author
