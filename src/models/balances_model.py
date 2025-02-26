from sqlmodel import Field, SQLModel, Column, Relationship
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy.types import Double, TIMESTAMP
from sqlalchemy.sql import func 
from src.models.loan_model import Loan
from datetime import datetime 

 

class Balances(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    month: str
    years: str
    income: float = Field(default=0.0, sa_column=Column(Double))
    expenses: float = Field(default=0.0, sa_column=Column(Double))
    month_balance : float = Field(default=0.0, sa_column=Column(Double))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now()))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now(), onupdate=func.now()))
    loan_id: int = Field(foreign_key="loan.id")
    loan: Optional["Loan"] = Relationship(back_populates="balances")
 