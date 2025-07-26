import requests
import api
import json


def getAPI():
    apiKey = api.getAPIKey()
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=50.04303&lon=-110.679016&appid={apiKey}")

#call all other methods and printing out our beautiful human readable shit
def main():
    data = getAPI()
    if data.status_code == 200:
        parsed = parseData(data)
        parsed[2] = round(kelvinToCel(float(parsed[2])))
        parsed[3] = round(kelvinToCel(float(parsed[3])))
        parsed[4] = round(kelvinToCel(float(parsed[4])))

        print(f"Sky: {parsed[0]}\nSky Description: {parsed[1]}\nCurrent Temp: {parsed[2]}\nLow Temp of: {parsed[3]}\nHigh Temp of: {parsed[4]}")
    else:
        print("some kind of error happened with getting the API data")

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

main()
