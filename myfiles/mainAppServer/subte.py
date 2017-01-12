import requests
import json
import conf

def getSubte():
    r = requests.get(conf.subteStatus)
    return r.json()

print(getSubte()["linea_c"])
