from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_create_type(client):
    response = client.post(
        '/types/',
        json={'id': 1, 'name': 'Type'},
    )

    assert response.status_code == 201
    assert response.json() == {'id': 1, 'name': 'Type'}


def test_read_types(client):
    response = client.get('/types/')
    assert response.status_code == 200
    assert response.json() == {'types': []}


def test_update_type(client, type):
    response = client.put(
        '/types/1',
        json={'id': 1, 'name': 'type test'},
    )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'type test'}


def test_delete_type(client, type):
    response = client.delete('/types/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'Type deleted'}
