import requests
import json
import conf

def getSubte():
    r = requests.get(conf.subteStatus)
    return r.json()

def getColorStatus(status):
    if status == "Normal":
        return "#33cc00"
    else:
        return "#df0101"
