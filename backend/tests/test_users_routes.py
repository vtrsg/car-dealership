from fastapi.testclient import TestClient

from backend.app import app
from backend.schemas import PublicUser

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


def test_read_users_with_users(client, user):
    user_schema = PublicUser.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'novo_nome',
            'phone': '55555555',
            'cpf': '55555555',
            'email': 'novo_email@example.com',
            'password': 'nova_senha',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'username': 'novo_nome',
        'phone': '55555555',
        'email': 'novo_email@example.com',
        'id': 1,
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}
