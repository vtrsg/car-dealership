from time import timezone

from sqlalchemy import select

from backend.models import Brand, Car, Location, ModelType, User


def test_create_user(session):
    new_user = User(
        id=1,
        username='test db user',
        password='secret',
        email='teste@test',
        phone='+5511999999999',
        cpf='000.000.000-00',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'test db user'))

    assert user.username == 'test db user'


def test_create_brand(session):
    new_brand = Brand(
        name='test db brand',
    )
    session.add(new_brand)
    session.commit()

    brand = session.scalar(select(Brand).where(Brand.name == 'test db brand'))

    assert brand.name == 'test db brand'


def test_create_type(session):
    new_type = ModelType(
        name='test db model type',
    )
    session.add(new_type)
    session.commit()

    type = session.scalar(
        select(ModelType).where(ModelType.name == 'test db model type')
    )

    assert type.name == 'test db model type'


def test_create_car(session, user: User, brand, type, location=Location):
    car = Car(
        name='Create Car',
        brand_id=brand.id,
        type_id=type.id,
        location=location.RS,
        year=2020,
        transmission='manual',
        price=55580.00,
        discount_price=5000.00,
        mileage=10000,
        color='black',
        created_date=f'{timezone}',
        image_path='http/localtest.com/images/image_name.png',
        seat=5,
        fuel='Gasolina',
        user_id=user.id,
    )

    session.add(car)
    session.commit()
    session.refresh(car)

    user = session.scalar(select(User).where(User.id == user.id))

    assert car in user.cars
