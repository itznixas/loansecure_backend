from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from datetime import datetime
from sqlalchemy.types import TIMESTAMP

class Client(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    lastname: str
    phone: int 
    registration_date: datetime = Field(default_factory=lambda: datetime.utcnow())

    loan_status: List["LoanStatus"] = Relationship(back_populates="client")
    loan: List["Loan"] = Relationship(back_populates= "client") 