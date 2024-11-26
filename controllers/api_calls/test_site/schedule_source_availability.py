from controllers.api.test_site.base_auth import BaseAuth
import requests
from utils.constants import URLs, Paths, Credentials

class ScheduleSourceAPI(BaseAuth):
    """Handles Schedule Source API interactions for employee availability"""
    
    def __init__(self):
        # Initialize with test site authentication
        super().__init__(
            auth_url=URLs.TEST_SITE_AUTH.value,
            credentials=Credentials.TEST_SITE
        )
        self.base_url = URLs.TEST_SITE_BASE.value
        
    def get_employee_availability(self, employee_id: str) -> dict:
        """
        Fetches an employee's availability ranges from Schedule Source
        
        Args:
            employee_id: Schedule Source external ID for the employee
            
        Returns:
            JSON response containing employee's availability ranges
        """
        try:
            headers = self.get_auth_headers()
            
            # Define query parameters for the request
            params = {
                'Fields': 'AvailableRanges,EmployeeExternalId',
                'EmployeeExternalId': employee_id
            }
            
            response = requests.get(
                f"{self.base_url}{Paths.SS_AVAILABILITY.value}",
                headers=headers,
                params=params
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Schedule Source API Error: {str(e)}")
            raise

if __name__ == "__main__":
    # Test the API functionality
    schedule_source = ScheduleSourceAPI()
    test_employee_id = "223133927"
    
    availability = schedule_source.get_employee_availability(test_employee_id)
    print("Employee Availability:", availability) 