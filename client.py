from dotenv import load_dotenv
import os
from base_client import BaseApiClient
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "")
USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")

# Ensure that the environment variables are set
if not BASE_URL or not USERNAME or not PASSWORD:
    raise ValueError("BASE_URL, USERNAME and PASSWORD must be set in the environment variables.")

class ApiClient(BaseApiClient):
    def __init__(self):
        super().__init__(BASE_URL)
        self.evidences_to_collect = 3  # change when needed

    def authenticate(self):
        response = self.post("auth/login", {
            "username": USERNAME,
            "password": PASSWORD
        })
        if "accessToken" not in response:
            raise Exception("Authentication failed: No accessToken in response")
        self.token = response["accessToken"]
