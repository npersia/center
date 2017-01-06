import requests
import json
import conf

#r = requests.get("http://localhost:8001/weathercondition?lat=-34.6421149&lon=-58.4612144")

def getWeather(lat,lon):
    r = requests.get(conf.weatherCondition+"?lat="+lat+"&lon="+lon)
    return r.json()


print(getWeather("-34.6421149","-58.4612144"))
