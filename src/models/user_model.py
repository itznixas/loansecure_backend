
from sqlmodel import Field, SQLModel, Column
from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional, Union
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func 

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, max_length=50, unique=True)  # Obligatorio
    hashed_password: str = Field(nullable=False)
    email: str = Field(index=True, unique=True)  # Obligatorio
    name: Optional[str] = None  # Opcional
    lastname: Optional[str] = None  # Opcional
    number_phone: Optional[str] = None  # Opcional
    disabled: bool = Field(default=False)  # Ahora el valor por defecto es False
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now()))

