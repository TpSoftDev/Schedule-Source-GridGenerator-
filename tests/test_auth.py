import sys
import os

# Add the parent directory to system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from controllers.api_calls.base_auth import BaseAuth
from controllers.utils.constants import URLs, Credentials

def test_authentication():
    """Test the authentication process"""
    
    # Initialize BaseAuth with test credentials
    auth = BaseAuth(
        auth_url=URLs.TEST_SITE_AUTH.value,
        credentials=Credentials.TEST_SITE
    )

    try:
        # Test authentication
        print("\nTesting authentication...")
        success = auth.authenticate()
        
        if success:
            print("✅ Authentication successful!")
            print(f"Session ID: {auth.session_id[:10]}...")  # Only show first 10 chars for security
            print(f"API Token: {auth.api_token[:10]}...")
            
            # Test getting headers
            headers = auth.get_auth_headers()
            print("\nGenerated Headers:")
            for key, value in headers.items():
                # Mask sensitive values
                if key in ['Authorization', 'SessionId']:
                    print(f"{key}: {value[:10]}...")
                else:
                    print(f"{key}: {value}")
                    
        else:
            print("❌ Authentication failed!")
            
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")

if __name__ == "__main__":
    test_authentication() 