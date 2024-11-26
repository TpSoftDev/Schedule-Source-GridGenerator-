from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()

class URLs(Enum):
    TEST_SITE_AUTH = os.getenv('TEST_SITE_AUTH')
    TEST_SITE_BASE = os.getenv('TEST_SITE_BASE')
    LIVE_SITE_BASE = os.getenv('LIVE_SITE_BASE')

class Paths(Enum):
    SS_AVAILABILITY = "/api/io/GlobalAvailDay/json"

class Credentials:
    TEST_SITE = {
        "code": os.getenv('SS_CODE'),
        "user": os.getenv('SS_USER'),
        "password": os.getenv('SS_PASSWORD')
    } 

def load_creds():
    creds = Credentials(
        os.getenv('SS_CODE'),
        os.getenv('SS_USER'),
        os.getenv('SS_PASSWORD')
    )
    return creds 