from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    cpf: Mapped[str]


class Brand(Base):
    __tablename__ = 'brands'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


# class Car(Base):
#     __tablename__ = 'cars'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     location: Mapped[str]
#     transmission: Mapped[str]
#     price: Mapped[float]
#     discount_price: Mapped[float]
#     mileage: Mapped[float]
#     color: Mapped[str]
#     seat: Mapped[int]
#     fuel: Mapped[str]
#     created_date: Mapped[str]
#     image_path: Mapped[str]
