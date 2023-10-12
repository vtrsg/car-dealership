from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_session
from backend.models import Brand, ModelType, User
from backend.schemas import (
    BrandList,
    BrandSchema,
    Message,
    ModelTypeList,
    ModelTypeSchema,
    PublicUser,
    UserList,
    UserSchema,
)

app = FastAPI()


"""
    User Routes
"""


@app.post('/users/', response_model=PublicUser, status_code=201)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(User.username == user.username)
    )

    if db_user:
        raise HTTPException(
            status_code=400, detail='Username already registered'
        )

    db_user = User(
        username=user.username,
        password=user.password,
        email=user.email,
        phone=user.phone,
        cpf=user.cpf,
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}


@app.put('/users/{user_id}', response_model=PublicUser)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):

    db_user = session.scalar(select(User).where(User.id == user_id))
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    db_user.username = user.username
    db_user.password = user.password
    db_user.email = user.email
    db_user.phone = user.phone
    db_user.cpf = user.cpf

    session.commit()
    session.refresh(db_user)

    return db_user


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    session.delete(db_user)
    session.commit()

    return {'detail': 'User deleted'}


"""
    Brand Routes
"""


@app.post('/brands/', response_model=BrandSchema, status_code=201)
def create_brand(brand: BrandSchema, session: Session = Depends(get_session)):
    db_brand = session.scalar(select(Brand).where(Brand.name == brand.name))

    if db_brand:
        raise HTTPException(status_code=400, detail='Brand already registered')

    db_brand = Brand(
        name=brand.name,
    )
    session.add(db_brand)
    session.commit()
    session.refresh(db_brand)

    return db_brand


@app.get('/brands/', response_model=BrandList)
def read_brands(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    brands = session.scalars(select(Brand).offset(skip).limit(limit)).all()
    return {'brands': brands}


@app.put('/brands/{brand_id}', response_model=BrandSchema)
def update_brand(
    brand_id: int, brand: BrandSchema, session: Session = Depends(get_session)
):

    db_brand = session.scalar(select(Brand).where(Brand.id == brand_id))
    if db_brand is None:
        raise HTTPException(status_code=404, detail='Brand not found')

    db_brand.name = brand.name

    session.commit()
    session.refresh(db_brand)

    return db_brand


@app.delete('/brands/{brand_id}', response_model=Message)
def delete_brand(brand_id: int, session: Session = Depends(get_session)):
    db_brand = session.scalar(select(Brand).where(Brand.id == brand_id))

    if db_brand is None:
        raise HTTPException(status_code=404, detail='Brand not found')

    session.delete(db_brand)
    session.commit()

    return {'detail': 'Brand deleted'}


"""
    TypeModel Routes
"""


@app.post('/types/', response_model=ModelTypeSchema, status_code=201)
def create_type(
    type: ModelTypeSchema, session: Session = Depends(get_session)
):
    db_type = session.scalar(
        select(ModelType).where(ModelType.name == type.name)
    )

    if db_type:
        raise HTTPException(status_code=400, detail='Type already registered')

    db_type = ModelType(
        name=type.name,
    )
    session.add(db_type)
    session.commit()
    session.refresh(db_type)

    return db_type


@app.get('/types/', response_model=ModelTypeList)
def read_types(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    types = session.scalars(select(ModelType).offset(skip).limit(limit)).all()
    return {'types': types}


@app.put('/types/{type_id}', response_model=ModelTypeSchema)
def update_type(
    type_id: int,
    type: ModelTypeSchema,
    session: Session = Depends(get_session),
):

    db_type = session.scalar(select(ModelType).where(ModelType.id == type_id))
    if db_type is None:
        raise HTTPException(status_code=404, detail='Type not found')

    db_type.name = type.name

    session.commit()
    session.refresh(db_type)

    return db_type


@app.delete('/types/{type_id}', response_model=Message)
def delete_type(type_id: int, session: Session = Depends(get_session)):
    db_type = session.scalar(select(ModelType).where(ModelType.id == type_id))

    if db_type is None:
        raise HTTPException(status_code=404, detail='Type not found')

    session.delete(db_type)
    session.commit()

    return {'detail': 'Type deleted'}
