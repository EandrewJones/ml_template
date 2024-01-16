"""
API Test Suite
--------------

Basic CRUD tests to ensure the endpoints are working as expected.

NOTE: If there are model unit tests in place, it may be a good idea to
mock the model responses with a fixture and just test the API business
logic to minimize resource usage.
"""
from fastapi.testclient import TestClient

from src.main import app  # Assuming your main FastAPI app file is named 'main'
from src.schema import ModelPayload

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Your API description here"}


def test_create_prediction():
    # NOTE: Needs to be updated to match your payload schema; consider using a fixture
    payload = {"data": [1, 2, 3]}
    response = client.post("/predict", json=ModelPayload(**payload).dict())
    assert response.status_code == 200
    assert "prediction" in response.json()


def test_invalid_payload():
    payload = {"invalid_key": "invalid_data"}
    response = client.post("/predict", json=payload)
    # Assumes there is built-in validation for the payload
    assert response.status_code == 422
