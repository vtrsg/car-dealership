from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_root_return_200():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
