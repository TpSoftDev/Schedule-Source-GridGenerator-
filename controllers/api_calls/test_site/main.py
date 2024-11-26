import requests
import json
import http
from urllib.parse import urlencode
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
external_directory = os.path.join(current_dir, "../..")
sys.path.append(external_directory)

from utils.Paths import Paths
from utils.URLs import URLs
from utils.helperFunctions import parse_tsv

# Needed for Mac
import certifi
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def authenticate():
    url = 'https://test.tmwork.net/2023.1'

    payload = json.dumps(
        {
            "ExternalId": "",
            "Request": {
                "Portal": "mgr",
                "Code": "ISU",
                "Username": "seans3",
                "Password": "8032",
            }
        }
    )

    headers = {
        "Content-Type": "application/json",
        "BuildCookie": "24060420361420.32735534d2ac453faeb6fc50bf314f4d",
        "Cookie": "BuildCookie=24060420361420.32735534d2ac453faeb6fc50bf314f4d",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()
    api_token = response_json["Response"]["APIToken"]
    session_id = response_json["Response"]["SessionId"]
    return {"sessionId": session_id, "apiToken": api_token}


#API call to get the global availability for a specific employee
#Param - employeeId - the external ID of the employee to look up
#Returns the employee's global availability data in JSON format
def getEmployeeAvailability(employeeId):
    credentials = authenticate("ISU", "seans3", "8032")
    conn = http.client.HTTPSConnection("test.tmwork.net")
    payload = ""

    headers = {
        "Content-Type": "application/json",
        "x-session-id": credentials["sessionId"],
        "x-api-token": credentials["apiToken"],
    }

    path = Paths.SS_AVAILABILITY.value
    query_params = {
        "Fields": "GlobalAvailDay",
        "EmployeeExternalId": employeeId
    }

    encoded_query_params = urlencode(query_params)
    url = f"{path}?{encoded_query_params}"
    
    conn.request(
        "GET",
        url,
        payload,
        headers,
    )
    
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)