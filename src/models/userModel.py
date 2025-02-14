from typing import Optional
from sqlmodel import Field, SQLModel
from database.database import meta


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, max_length=50, unique=True)
    email: str = Field(index=True, unique=True)
    name: str = Field(index = True)
    lastaname: str
    number_phone: str
    password: str

    def check_password(self,password: str) -> bool:
        return self.password == password

