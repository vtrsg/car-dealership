import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.app import app
from backend.database import get_session
from backend.models import Base, Brand, Car, Location, ModelType, User
from backend.security import get_password_hash


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    yield Session()

    Base.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token/',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']


@pytest.fixture
def user(session):
    user = User(
        username='Teste',
        email='teste@test.com',
        password=get_password_hash('testtest'),
        phone='test',
        cpf='test',
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'testtest'

    return user


@pytest.fixture
def brand(session):
    brand = Brand(
        name='Teste',
    )
    session.add(brand)
    session.commit()
    session.refresh(brand)

    return brand


@pytest.fixture
def type(session):
    type = ModelType(
        name='SUV',
    )
    session.add(type)
    session.commit()
    session.refresh(type)

    return type


@pytest.fixture
def car(session, user: user, brand: brand, type: type):
    car = Car(
        name='Car',
        brand_id=brand.id,
        type_id=type.id,
        location=Location.RS,
        year=2020,
        transmission='auto',
        price=55500,
        discount_price=5000,
        mileage=100000,
        color='black',
        seat=5,
        fuel='gas',
        created_date='time',
        image_path='https://localhost.com/images/img_car.png',
        user_id=user.id,
    )
    session.add(car)
    session.commit()
    session.refresh(car)

    return car
