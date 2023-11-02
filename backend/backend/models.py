from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Location(str, Enum):
    RS = 'Rio grande do Sul'
    SP = 'São Paulo'
    SC = 'Santa Catarina'


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    cpf: Mapped[str] = mapped_column(unique=True, index=True)

    cars = relationship(
        'Car', back_populates='user', cascade='all, delete-orphan'
    )


class Brand(Base):
    __tablename__ = 'brands'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class ModelType(Base):
    __tablename__ = 'types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    brand_id: Mapped[int] = mapped_column(ForeignKey('brands.id'))
    type_id: Mapped[int] = mapped_column(ForeignKey('types.id'))
    location: Mapped[Location]
    year: Mapped[int]
    transmission: Mapped[str]
    price: Mapped[float]
    discount_price: Mapped[float]
    mileage: Mapped[float]
    color: Mapped[str]
    seat: Mapped[int]
    fuel: Mapped[str]
    created_date: Mapped[str]
    image_path: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)

    user: Mapped[User] = relationship(back_populates='cars')
