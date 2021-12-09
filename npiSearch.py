import sys
import requests
import json

url = "https://npiregistry.cms.hhs.gov/api/?version=2.1&number="
doctorDict = {
    "first_name" : "",
    "last_name" : "",
    "address_1" : "",
    "address_2" : "",
    "city" : "",
    "state" : "",
    "zip" : "",
    "phone_number" : "",

}

params = dict(
    version=2.1,
    number=1780951947
)
def getDrInfo(npi):

    params["number"] = npi
    resp = requests.get(url=url, params=params)
    data = resp.json()
    try:
        doctorDict["first_name"] = data["results"][0]["basic"]["first_name"]
        doctorDict["last_name"] = data["results"][0]["basic"]["last_name"]
    except:
        doctorDict["first_name"] = data["results"][0]["basic"]["authorized_official_first_name"]
        doctorDict["last_name"] = data["results"][0]["basic"]["authorized_official_last_name"]
    doctorDict["address_1"] = data["results"][0]["addresses"][0]["address_1"]
    doctorDict["address_2"] = data["results"][0]["addresses"][0]["address_2"]
    doctorDict["city"] = data["results"][0]["addresses"][0]["city"]
    doctorDict["state"] = data["results"][0]["addresses"][0]["state"]
    doctorDict["zip"] = data["results"][0]["addresses"][0]["postal_code"]
    doctorDict["phone_number"] = data["results"][0]["addresses"][0]["telephone_number"]

    return doctorDict

#items = json.loads(data)
