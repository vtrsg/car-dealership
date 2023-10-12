from sqlalchemy import select

from backend.models import User


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
