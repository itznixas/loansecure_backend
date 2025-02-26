from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreateShema(BaseModel):
    username: str
    email: EmailStr
    password: str
    disabled: Optional[bool] = False

    class Config:
        orm_mode = True 

class UserResponseSchema(BaseModel):
    message: str
    user_id: int
    username: str
    email: EmailStr
    created_at: datetime
    disabled: Optional[bool] = False

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
    disabled: Optional[bool] = False

class UserDisableSchema(BaseModel):
    disable: Optional[bool] = True