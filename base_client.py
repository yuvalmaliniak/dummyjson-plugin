import requests

class BaseApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def get(self, endpoint):
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        response = requests.get(f"{self.base_url}/{endpoint}", headers=headers)
        self.handle_error(response)
        try:
            return response.json()
        except ValueError:
            raise Exception(f"Invalid JSON response: {response.text}")

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        self.handle_error(response)
        try:
            return response.json()
        except ValueError:
            raise Exception(f"Invalid JSON response: {response.text}")

    def handle_error(self, response):
        status = response.status_code
        text = response.text
        if status == 400:
            raise Exception(f"Bad Request (400): {text}")
        elif status == 401:
            raise Exception(f"Unauthorized (401): Check credentials (also check your .env file).")
        elif status == 403:
            raise Exception(f"Forbidden (403): You don't have access.")
        elif status == 404:
            raise Exception(f"Not Found (404): Endpoint may be incorrect.")
        elif 500 <= status < 600:
            raise Exception(f"Server Error ({status}): Try again later.")
        elif status != 200:
            raise Exception(f"Unexpected Error ({status}): {text}")
