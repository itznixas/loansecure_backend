from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated  # Cambia esto si usabas typing_extensions
from fastapi import Depends
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://royerjrr:Kira1515@db:3306/loansecure")


engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]  # Asegúrate de que Session esté definido antes de esta línea
