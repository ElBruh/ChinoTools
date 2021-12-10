import sys
import requests
import json
import string

url = "http://icd10api.com/"
icdDict = {
    "Name" : "",
    "Description":"",
}

params = dict(
    code="",
    desc="short",
    r="json"
)

def getICDInfo(icd):
    #finalICD = icd.translate(str.maketrans('', '', '.!@#$'))
    #print(finalICD)
    params["code"] = icd
    resp = requests.get(url=url, params=params)
    data = resp.json()
    #print(data)
    
    try:
        icdDict["Name"] = data["Name"]
        icdDict["Description"] = data["Description"]
    except:
        icdDict["Name"] = data["Name"]
        icdDict["Description"] = data["Description"]
    #print(icdDict["Description"])
    return icdDict
    

#print(getNPIInfo("M62.81"))