from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreateShema(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True 

class UserResponseSchema(BaseModel):
    message: str
    user_id: int
    username: str
    email: EmailStr
    created_at: datetime