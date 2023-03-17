/*
 * CarbonAware.WebApi, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: 1.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package client

import (
	"time"
)

type CarbonIntensityDto struct {
	// the location name where workflow is run
	Location string `json:"location,omitempty"`
	// the time at which the workflow we are measuring carbon intensity for started
	StartTime time.Time `json:"startTime,omitempty"`
	// the time at which the workflow we are measuring carbon intensity for ended
	EndTime time.Time `json:"endTime,omitempty"`
	// Value of the marginal carbon intensity in grams per kilowatt-hour.
	CarbonIntensity float64 `json:"carbonIntensity,omitempty"`
}
