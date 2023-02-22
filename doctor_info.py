import requests
import json

# Set the base URL for the API
API_BASE_URL = "https://www.hipaaspace.com/api/npi/search"

# Set the token for the API
TOKEN = "4F92BE926DA7401E96561F9AB7996E0493247313F16845F8B40CAF1A80B9D065"

# Set the parameters for the API call
params = {
    "q": "",
    "rt": "json",
    "token": TOKEN
}

# Define a function to get a doctor's information
def get_doctor_info(npi):
    # Set the NPI number as the search query
    params["q"] = npi

    # Make the API call and get the response
    response = requests.get(API_BASE_URL, params=params)

    # Check the status code of the response
    if response.status_code != 200:
        print(f"Error: API returned status code {response.status_code}")
        return None

    # Load the JSON response into a dictionary
    data = response.json()

    # Extract the relevant information and store it in a dictionary
    doctor = {
        "first_name": "",
        "last_name": "",
        "address_1": data["NPI"][0]["FirstLinePracticeLocationAddress"],
        "city": data["NPI"][0]["PracticeLocationAddressCityName"],
        "state": data["NPI"][0]["PracticeLocationAddressStateName"],
        "zip": data["NPI"][0]["PracticeLocationAddressPostalCode"],
        "phone_number": data["NPI"][0]["PracticeLocationAddressTelephoneNumber"],
    }

    # Try to get the first and last name of the doctor from the data
    try:
        doctor = {
            "first_name": data["NPI"][0]["FirstName"],
            "last_name": data["NPI"][0]["LastName"],
        }
    # If the first and last name are not available, use the first and last name of the authorized official
    except:
        doctor["first_name"] = data["NPI"][0]["AuthorizedOfficialFirstName"]
        doctor["last_name"] = data["NPI"][0]["AuthorizedOfficialLastName"]

    # Return the dictionary containing the doctor's information
    return doctor

# Test the function with a sample NPI
#doctor_info = get_doctor_info("1932526456")
#print(doctor_info)
