from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    phone: str
    cpf: str


class PublicUser(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: str
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[PublicUser]


class Message(BaseModel):
    detail: str


class BrandSchema(BaseModel):
    id: int
    name: str


class BrandList(BaseModel):
    brands: list[BrandSchema]


class ModelTypeSchema(BaseModel):
    id: int
    name: str


class ModelTypeList(BaseModel):
    types: list[ModelTypeSchema]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class CarSchema(BaseModel):
    id: int
    name: str
    brand_id: int
    type_id: int
    location: str
    year: int
    transmission: str
    price: float
    discount_price: float
    mileage: float
    color: str
    seat: int
    fuel: str
    created_date: str
    image_path: str
    user_id: int


class CarList(BaseModel):
    cars: list[CarSchema]
