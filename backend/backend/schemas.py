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
