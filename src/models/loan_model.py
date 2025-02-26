from sqlmodel import Field, SQLModel, Column, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

#from src.models.payments_model import Payments
from sqlalchemy.types import Double, TIMESTAMP
from sqlalchemy.sql import func 



   

class Loan(SQLModel, table=True):
    id: Optional[int] = Field(default = None, primary_key = True)
    amount: float = Field(default=0.0, sa_column=Column(Double))
    interest_rate: float = Field(default=0.0, sa_column=Column(Double))
    deadline: int

    start_date: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(TIMESTAMP))
    expiration_date: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(TIMESTAMP))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now()))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now(), onupdate=func.now()))
    client_id: int = Field(foreign_key="client.id")
    loan_status_id: int = Field(foreign_key="loanstatus.id")
    loanStatus: Optional["LoanStatus"] = Relationship(back_populates="loan")
    client: Optional["Client"] = Relationship(back_populates="loan")
    payments: List["Payments"] = Relationship(back_populates="loan")   
    balances: List["Balances"] = Relationship(back_populates="loan")