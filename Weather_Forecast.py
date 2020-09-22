"""
Date: August 2018
This is a weather forecast program, which asks the user for a location.
Based on the input, it pulls data from the Openweathermap API.
The API request works with either location name or zip code.
"""


import requests
import json


def weather_forecast():
    url = "http://api.openweathermap.org/data/2.5/weather?&APPID=ef2ee06802bac386afc8272d6b3dc426&units=metric&q="

    '''
    Error Handling depending on the status code of the API:
    if the response status code is 200, meaning the location exists, the loop will break and the program will continue
    with the extraction of information. If the location does not exists, a KeyError will be raised and the user 
    is asked again.
    '''
    while True:
        try:
            city = str(input("Please enter the name of a location to get a weather forecast: "))
            specified_url = url + city
            response = requests.get(specified_url)
            data = response.text
            weather = json.loads(data)
            if response.status_code == 200:
                break
            else:
                raise KeyError
        except KeyError:
            if response.status_code == 404:
                print("This location does not exist. Please try again.")
                continue
        else:
            break

    # Extraction of information

    'This line just divides the input from the output.'
    print("--------------------------------------------")

    'This part extracts the country information from the API Data'
    country_info = weather["sys"]["country"]
    print("Here is the current weather for", city, ",", country_info, ":\n")

    'This part extracts the description of the weather condition from the API Data'
    weather_cond = weather["weather"][0]["description"]
    print("Weather Condition: ", weather_cond)

    'This part extracts the cloudiness information from the API Data'
    clouds = weather["clouds"]["all"]
    print("Cloudiness: ", clouds, "%")

    'This part extracts the current temperature as well as the minimum and maximum temperature'
    temp = weather["main"]["temp"]
    print("Current Temperature: ", temp)
    temp_min = weather["main"]["temp_min"]
    print("Minimum Temperature: ", temp_min)
    temp_max = weather["main"]["temp_max"]
    print("Maximum Temperature: ", temp_max)


weather_forecast()
