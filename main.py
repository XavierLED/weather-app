import requests
import api
import json

def getAPI(location):
    apiKey = api.getAPIKey()
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}")

def main(city):
    data = getAPI(city)
    if data.status_code == 200:
        parsed = parseData(data)
        parsed[2] = round(kelvinToCel(float(parsed[2])))
        parsed[3] = round(kelvinToCel(float(parsed[3])))
        parsed[4] = round(kelvinToCel(float(parsed[4])))

        return [f"Sky: {parsed[0]}"], [f"Sky Description: {parsed[1]}"], [f"Current Temp: {parsed[2]}"], [f"Low Temp of: {parsed[3]}"], [f"High Temp of: {parsed[4]}"]
    elif data.status_code == 401:
        return "some kind of error happened with getting the API data"
    elif data.status_code == 404:
        return "entered in invalid city name"
    else:
        return "some unknown reason is messing with request"

def parseData(data):
    data = data.text
    looking = ['"main"', '"description"', '"temp"', '"temp_min"', '"temp_max"']

    data = json.loads(data)
    looking[0] = data["weather"][0]["main"]
    looking[1] = data["weather"][0]["description"]
    looking[2] = data["main"]["temp"]
    looking[3] = data["main"]["temp_min"]
    looking[4] = data["main"]["temp_max"]

    return  looking

def kelvinToCel(kelvin):
    celcius = kelvin - 273
    return celcius
