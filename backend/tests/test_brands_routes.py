from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_create_brand(client):
    response = client.post(
        '/brands/',
        json={'id': 1, 'name': 'brand test'},
    )

    assert response.status_code == 201
    assert response.json() == {'id': 1, 'name': 'brand test'}


def test_read_brands(client):
    response = client.get('/brands/')
    assert response.status_code == 200
    assert response.json() == {'brands': []}


def test_update_brand(client, brand):
    response = client.put(
        '/brands/1',
        json={'id': 1, 'name': 'brand test'},
    )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'name': 'brand test'}


def test_delete_brand(client, brand):
    response = client.delete('/brands/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'Brand deleted'}