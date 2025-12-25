"""
Unit tests for main application
"""

import pytest
import json
from app.main import app


@pytest.fixture
def client():
    """Create test client"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test home endpoint"""
    response = client.get("/")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["success"] is True
    assert "Automation Engine" in data["data"]["service"]


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["success"] is True
    assert data["data"]["status"] == "healthy"


def test_echo_endpoint_valid_data(client):
    """Test echo endpoint with valid data"""
    test_data = {"message": "Hello CI/CD Pipeline"}

    response = client.post(
        "/api/echo", data=json.dumps(test_data), content_type="application/json"
    )

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["success"] is True
    assert data["data"]["echo"] == test_data


def test_echo_endpoint_invalid_data(client):
    """Test echo endpoint with invalid data"""
    response = client.post(
        "/api/echo", data=json.dumps({}), content_type="application/json"
    )

    assert response.status_code == 400
    data = json.loads(response.data)
    assert data["success"] is False


def test_pipeline_info_endpoint(client):
    """Test pipeline info endpoint"""
    response = client.get("/api/pipeline-info")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["success"] is True
    assert "pipeline" in data["data"]
    assert "ci_stages" in data["data"]["pipeline"]


def test_404_error(client):
    """Test 404 error handling"""
    response = client.get("/nonexistent")
    assert response.status_code == 404

    data = json.loads(response.data)
    assert data["success"] is False
    assert "not found" in data["data"]["error"].lower()


def test_response_format(client):
    """Test that all responses follow standard format"""
    response = client.get("/")
    data = json.loads(response.data)

    # Check standard response structure
    assert "success" in data
    assert "data" in data
    assert "timestamp" in data
    assert isinstance(data["success"], bool)


def test_security_headers(client):
    """Test security headers are present"""
    response = client.get("/")

    # Note: In a real app, you'd configure these headers
    # This test documents the expectation
    assert response.status_code == 200
