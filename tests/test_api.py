import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """
    Test the GET / health endpoint.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_success():
    """
    Test the POST /predict endpoint with valid input.
    """
    response = client.post("/predict", json={"hours_studied": 5.0})
    assert response.status_code == 200
    data = response.json()
    assert "predicted_score" in data
    # Based on our synthetic data: score = 10 * 5 + 5 = 55
    assert data["predicted_score"] == pytest.approx(55.0)

def test_predict_negative_hours():
    """
    Test the POST /predict endpoint with invalid (negative) input.
    """
    response = client.post("/predict", json={"hours_studied": -1.0})
    # FastAPI returns 422 Unprocessable Entity for validation errors
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["type"] == "greater_than_equal"

def test_predict_invalid_input():
    """
    Test the POST /predict endpoint with non-numeric input.
    """
    response = client.post("/predict", json={"hours_studied": "not a number"})
    assert response.status_code == 422
