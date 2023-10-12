from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'secret',
            'phone': '5555555555',
            'cpf': '000000000',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'string',
        'email': 'user@example.com',
        'phone': '5555555555',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'put string',
            'email': 'put@example.com',
            'password': 'newpassword',
            'phone': '55555555',
            'cpf': '55555555',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'username': 'put string',
        'email': 'put@example.com',
        'phone': '55555555',
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


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
