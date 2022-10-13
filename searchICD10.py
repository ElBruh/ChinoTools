import sys
import requests
import json
import string

url = "http://icd10api.com/"
icdDict = {
    "Name" : "",
    "Description":"",
    "Valid": "",
    "Note": "",
    "ConsiderationName": "",
    "ConsiderationDescription": "",
}

params = dict(
    code="",
    desc="short",
    r="json"
)
token="4F92BE926DA7401E96561F9AB7996E0493247313F16845F8B40CAF1A80B9D065"

def getICDInfo(icd):
    #finalICD = icd.translate(str.maketrans('', '', '.!@#$'))
    #print(finalICD)
    #params["code"] = icd
    resp = requests.get("https://www.hipaaspace.com/api/icd10/search?q={}&rt=json&token={}".format(icd, token))
    data = resp.json()
    print(data)
    
  
    icdDict["Name"] = data["ICD10"][0]["Code"]
    icdDict["Description"] = data["ICD10"][0]["Description"]
    icdDict["Valid"] = data["ICD10"][0]["ValidForSubmissionOnUB04"]
    icdDict["Note"] = data["ICD10"][0]["Note"]

    for hcpcs in data["ICD10"]:
        if(hcpcs["ValidForSubmissionOnUB04"] == "true"):
            print(hcpcs["Code"])
            print(hcpcs["Description"])
            icdDict["ConsiderationName"] = hcpcs["Code"]
            icdDict["ConsiderationDescription"] = hcpcs["Description"]
            break
    #if(icdDict["Valid"] == "False"):
    #    raise ValueError("Icd 10 code is not valid for billing")
    #    return icdDict
    
    #print(icdDict["Description"])
    print(icdDict)
    return icdDict
    

#print(getNPIInfo("M62.81"))