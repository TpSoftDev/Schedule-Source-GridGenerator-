import os
import sys

# Add the parent directory to system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now import the Auth class
from test_site.utils.auth import Auth
import json

def getEmployeeAvailability(employeeId):
    """
    Gets employee availability using authenticated API call
    """
    auth = Auth()
    
    if not auth.authenticate():
        print("❌ Authentication failed")
        return None

    try:
        base_url = URLs.TEST_SITE_AUTHENTICATE.value.replace('/api/ops/auth', '')
        url = f"{base_url}/2023.1/api/io/GlobalAvailDay/"
        
        params = {
            "AvailableRanges": "",
            "EmployeeExternalId": employeeId
        }
        
        headers = auth.get_auth_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        availability_data = response.json()
        print("\n📊 Availability Data:")
        print(json.dumps(availability_data, indent=2))
        
        return availability_data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to get availability: {str(e)}")
        return None

if __name__ == "__main__":
    print("🔍 Fetching availability for employee...")
    result = getEmployeeAvailability("944816917")
    if result:
        print("\n✅ Successfully retrieved availability")
