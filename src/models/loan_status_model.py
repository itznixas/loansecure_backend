from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class LoanStatus(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str   
    
    client_id: int = Field(foreign_key="client.id")  # Clave foránea correcta
    client: Optional["Client"] = Relationship(back_populates="loan_status")
    loan: List["Loan"] = Relationship(back_populates= "loan_status") 