import requests
from .exceptions import (
    AidnoxAPIError,
    AuthenticationError,
    RateLimitError,
    BadRequestError,
    NotFoundError
)

class AidnoxClient:
    def __init__(self, api_key: str, base_url: str = "https://api.aidnox.com/v1", timeout=0.0):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.timeout = timeout

    def diagnose_symptoms(self, symptoms: str):
        """Send symptom text to Aidnox API and get diagnosis."""
        url = f"{self.base_url}/diagnosis/text"
        response = requests.post(url, headers=self.headers, json={"symptoms": symptoms})
        return self._handle_response(response)

    def diagnose_image(self, image_path: str):
        """Send an image to Aidnox API and get visual diagnosis."""
        url = f"{self.base_url}/diagnosis/image"
        with open(image_path, "rb") as image_file:
            files = {"image": image_file}
            response = requests.post(url, headers={"Authorization": self.headers["Authorization"]}, files=files)
        return self._handle_response(response)

    def get_diagnosis_history(self):
        """Get previous diagnosis history from user."""
        url = f"{self.base_url}/history"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 401:
            raise AuthenticationError("Unauthorized: Invalid API key or token.", response.status_code, response.text)
        elif response.status_code == 429:
            raise RateLimitError("Rate limit exceeded. Try again later.", response.status_code, response.text)
        elif response.status_code == 400:
            raise BadRequestError("Bad request. Check your parameters.", response.status_code, response.text)
        elif response.status_code == 404:
            raise NotFoundError("Resource not found.", response.status_code, response.text)
        elif not response.ok:
            raise AidnoxAPIError(f"Unexpected error: {response.text}", response.status_code, response.text)
        return response.json()
