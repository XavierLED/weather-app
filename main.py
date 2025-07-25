import requests
import api


def getAPI():
    apiKey = api.getAPIKey()
    return f"https://api.openweathermap.org/data/2.5/weather?lat=50.04303&lon=-110.679016&appid={apiKey}"

#call all other methods and printing out our beautiful human readable shit
def main():
    data = getAPI()
    print(data)
    parsed = parseData(data)

def parseData(data):
    print(data)
    return data

