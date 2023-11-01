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
