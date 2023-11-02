from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_session
from backend.models import Car
from backend.schemas import CarList, CarSchema, Message

Session = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix='/cars', tags=['cars'])


@router.post('/', response_model=CarSchema, status_code=201)
def car(car: CarSchema, session: Session):
    db_car = session.scalar(
        select(Car).where(Car.name == car.name and Car.user_id == car.user_id)
    )

    if db_car:
        raise HTTPException(status_code=400, detail='Car already registered')

    db_car = Car(
        name=car.name,
        brand_id=car.brand_id,
        type_id=car.type_id,
        location=car.location,
        year=car.year,
        transmission=car.transmission,
        price=car.price,
        discount_price=car.discount_price,
        mileage=car.mileage,
        color=car.color,
        seat=car.seat,
        fuel=car.fuel,
        created_date=car.created_date,
        image_path=car.image_path,
        user_id=car.user_id,
    )
    session.add(db_car)
    session.commit()
    session.refresh(db_car)

    return db_car


@router.get('/', response_model=CarList)
def read_cars(session: Session, skip: int = 0, limit: int = 100):
    cars = session.scalars(select(Car).offset(skip).limit(limit)).all()
    return {'cars': cars}


@router.put('/{car_id}', response_model=CarSchema)
def update_car(car_id: int, car: CarSchema, session: Session):

    db_car = session.scalar(select(Car).where(Car.id == car_id))
    if db_car is None:
        raise HTTPException(status_code=404, detail='Car not found')

    db_car.name = car.name

    session.commit()
    session.refresh(db_car)

    return db_car


@router.delete('/{car_id}', response_model=Message)
def delete_car(car_id: int, session: Session):
    db_car = session.scalar(select(Car).where(Car.id == car_id))

    if db_car is None:
        raise HTTPException(status_code=404, detail='Car not found')

    session.delete(db_car)
    session.commit()

    return {'detail': 'Car deleted'}
