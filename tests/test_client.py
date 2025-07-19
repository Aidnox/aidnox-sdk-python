import pytest
from aidnox_sdk import AidnoxClient
from aidnox_sdk.exceptions import AidnoxAPIError

import os

# Mocking requests
import requests
import requests_mock

API_KEY = "test_api_key"
BASE_URL = "https://api.aidnox.ai/v1"


@pytest.fixture
def client():
    return AidnoxClient(api_key=API_KEY, base_url=BASE_URL)


def test_client_initialization(client):
    assert client.api_key == API_KEY
    assert client.base_url == BASE_URL


def test_diagnose_symptoms_success(client):
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/diagnose/text", json={"diagnosis": "Malaria", "confidence": 0.85})

        response = client.diagnose_symptoms("I have fever and chills")
        assert response["diagnosis"] == "Malaria"
        assert response["confidence"] == 0.85


def test_diagnose_symptoms_empty_input(client):
    with pytest.raises(ValueError, match="Symptom text must be a non-empty string"):
        client.diagnose_symptoms("")


def test_diagnose_image_success(client, tmp_path):
    dummy_image = tmp_path / "image.jpg"
    dummy_image.write_bytes(b"fake-image-data")

    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/diagnose/image", json={"diagnosis": "Skin Infection", "confidence": 0.77})
        response = client.diagnose_image(str(dummy_image))

        assert response["diagnosis"] == "Skin Infection"
        assert response["confidence"] == 0.77


def test_diagnose_image_file_not_found(client):
    with pytest.raises(FileNotFoundError):
        client.diagnose_image("non_existing_image.jpg")


def test_custom_timeout_setting():
    client = AidnoxClient(api_key="123", timeout=15)
    assert client.timeout == 15


def test_error_handling_invalid_json(client):
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/diagnose/text", text="not json", status_code=200)

        with pytest.raises(AidnoxAPIError):
            client.diagnose_symptoms("fever")


def test_error_handling_http_error(client):
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/diagnose/text", status_code=500, json={"error": "Internal Server Error"})

        with pytest.raises(AidnoxAPIError) as e:
            client.diagnose_symptoms("fever")
        assert "API Error" in str(e.value)
