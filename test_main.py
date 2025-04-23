import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert b"OK" in response.data
