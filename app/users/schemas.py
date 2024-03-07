from enum import Enum
from pydantic import BaseModel, EmailStr

    

class SUserLogin(BaseModel):
    email: EmailStr
    password: str

class SUserBase(BaseModel):
    email: EmailStr
    name: str
    role: str


class SUserAuth(SUserBase):
    password: str


class SUserDB(SUserBase):
    hashed_password: str
