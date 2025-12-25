"""
Test configuration and fixtures
"""

import pytest
import os
import sys

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture(scope="session")
def app_config():
    """Application configuration for testing"""
    return {"TESTING": True, "SECRET_KEY": "test-secret-key", "DEBUG": True}


@pytest.fixture
def sample_data():
    """Sample data for testing"""
    return {
        "message": "Hello CI/CD Pipeline",
        "user": "test-user",
        "timestamp": "2024-01-01T00:00:00Z",
    }


@pytest.fixture
def invalid_data():
    """Invalid data for testing error cases"""
    return [None, {}, "", []]
