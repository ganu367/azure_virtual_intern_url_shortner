from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field
from typing import List


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    username: EmailStr
    password: str
    confirm_password: str

    class config:

        orm_mode = True


class UserPassword(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str


class ForgetPassword(BaseModel):
    new_password: str
    confirm_password: str

    class config:
        orm_mode = True


class UrlCreate(BaseModel):
    original_url: str


class UrlUpdateCount(BaseModel):
    click_count: int


class UrlUpdate(BaseModel):
    key_url: str


class contactUsBase(BaseModel):
    name: str
    email: str


class contactUsCreate(contactUsBase):
    mobile_number: int
    messages: str

    class config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user: Union[dict, None] = None
