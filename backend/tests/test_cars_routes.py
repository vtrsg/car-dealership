from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_create_car(client):
    response = client.post(
        '/cars/',
        json={
            'id': 1,
            'name': 'car test',
            'brand_id': 1,
            'type_id': 1,
            'location': 'RS',
            'year': 2020,
            'transmission': 'auto',
            'price': 50000,
            'discount_price': 10000,
            'mileage': 100000,
            'color': 'black',
            'seat': 5,
            'fuel': 'auto',
            'created_date': 'date',
            'image_path': 'https://localhost.com/images/img_car.png',
            'user_id': 1,
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'name': 'car test',
        'brand_id': 1,
        'type_id': 1,
        'location': 'Rio grande do Sul',
        'year': 2020,
        'transmission': 'auto',
        'price': 50000,
        'discount_price': 10000,
        'mileage': 100000,
        'color': 'black',
        'seat': 5,
        'fuel': 'auto',
        'created_date': 'date',
        'image_path': 'https://localhost.com/images/img_car.png',
        'user_id': 1,
    }


def test_read_cars(client):
    response = client.get('/cars/')
    assert response.status_code == 200
    assert response.json() == {'cars': []}


def test_update_car(client, car):
    response = client.put(
        f'/cars/{car.id}',
        json={
            'id': 1,
            'name': 'car test put',
            'brand_id': 1,
            'type_id': 1,
            'location': 'RS',
            'year': 2020,
            'transmission': 'auto',
            'price': 50000,
            'discount_price': 10000,
            'mileage': 100000,
            'color': 'black',
            'seat': 5,
            'fuel': 'auto',
            'created_date': 'date',
            'image_path': 'https://localhost.com/images/img_car.png',
            'user_id': 1,
        },
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'car test put'


def test_delete_car(client, car):
    response = client.delete(
        f'/cars/{car.id}',
    )
    assert response.status_code == 200
    assert response.json() == {'detail': 'Car deleted'}
