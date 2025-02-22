from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional, Union

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, max_length=50, unique=True)  # Obligatorio
    hashed_password: str = Field(nullable=False)
    email: str = Field(index=True, unique=True)  # Obligatorio
    name: Optional[str] = None  # Opcional
    lastname: Optional[str] = None  # Opcional
    number_phone: Optional[str] = None  # Opcional
    disabled: Union[bool, None] = None  # Opcional
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow())



class UserCreate(SQLModel):
    username: str
    email: str
    password: str #no se guarda a la base de datos

class UserResponse(SQLModel):
    id: int
    username: str
    email: str
    created_at: datetime    