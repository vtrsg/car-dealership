from sqlalchemy import select

from backend.models import Brand, ModelType, User


def test_create_user(session):
    new_user = User(
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
