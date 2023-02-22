from asyncio.windows_events import NULL
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

token="4F92BE926DA7401E96561F9AB7996E0493247313F16845F8B40CAF1A80B9D065"

params = dict(
    version=2.1,
    number=1780951947,
    token="4F92BE926DA7401E96561F9AB7996E0493247313F16845F8B40CAF1A80B9D065"
)
def getDrInfo(npi):
    
    #params["number"] = npi
    resp = requests.get("https://www.hipaaspace.com/api/npi/search?q={}&rt=json&token={}".format(npi, token))
    print(resp)
    data = resp.json()
    print(data)
    try:
        doctorDict["first_name"] = data["NPI"][0]["FirstName"]
        doctorDict["last_name"] = data["NPI"][0]["LastName"]
        
        
    except:
        doctorDict["first_name"] = data["NPI"][0]["AuthorizedOfficialFirstName"]
        doctorDict["last_name"] = data["NPI"][0]["AuthorizedOfficialLastName"]
    
    doctorDict["address_1"] = data["NPI"][0]["FirstLinePracticeLocationAddress"]
    doctorDict["city"] = data["NPI"][0]["PracticeLocationAddressCityName"]
    doctorDict["state"] = data["NPI"][0]["PracticeLocationAddressStateName"]
    doctorDict["zip"] = data["NPI"][0]["PracticeLocationAddressPostalCode"]
    doctorDict["phone_number"] = data["NPI"][0]["PracticeLocationAddressTelephoneNumber"]

    return doctorDict

#items = json.loads(data)
#print("Enter the NPI You want to search: ")
#npi = input()
#print(getDrInfo(npi))