from sqlalchemy import select

from backend.models import Brand, User


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
