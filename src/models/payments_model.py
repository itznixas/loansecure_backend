from sqlmodel import Field, SQLModel, Relationship, Column
from typing import List, Optional
from datetime import datetime 
from sqlalchemy.types import Double, TIMESTAMP
from sqlalchemy.sql import func 

class Payments(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount_paid: float = Field(default=0.0, sa_column=Column(Double))
    type_payment: float = Field(default=0.0, sa_column=Column(Double))
    form_payment: str
    date: datetime
    remaining_balance: float = Field(default=0.0, sa_column=Column(Double))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now()))
    updated_at: datetime | None = Field(default=None, 
    sa_column=Column(TIMESTAMP, nullable=True, server_default=func.now(), onupdate=func.now()))
    loan_id: int = Field(foreign_key="loan.id")
    loan: Optional["Loan"] = Relationship(back_populates="payments")

  