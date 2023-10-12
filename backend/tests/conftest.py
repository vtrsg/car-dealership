import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.app import app
from backend.database import get_session
from backend.models import Base, Brand, User


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
def user(session):
    user = User(
        username='Teste',
        email='teste@test.com',
        password='testtest',
        phone='test',
        cpf='test',
    )
    session.add(user)
    session.commit()
    session.refresh(user)

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
