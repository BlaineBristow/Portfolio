# Obtaining Weather Conditions From Weather API

## Introduction
This program is intended to be run and return the weather forecast for a location in the United States (based either on zip code or city and state) given by the user. The data is pulled in real time from an api, the location is provided by the user, and the forecast and current conditions are returned to the user.

## Methods
This program returns the current weather for a location within the US, first prompting the user to choose zip code or city and state lookup, then prompting for the location info before hitting a location lookup api. The latitude and longitude returned from the api, and the user is prompted for temperature units. The latitude, longitude, and units are fed into another api, which returns the weather data for that location. The api response is then fed into another function which returns a user-friendly print of the data. After receiving the weather data, the user is prompted to repeat the process or quit.
