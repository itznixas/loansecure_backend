from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.database.database import engine



router = APIRouter(prefix="/users") 

@router.get("/test-db")
def test_db_connection():
    try:
        with Session(engine) as session:
            session.exec("SELECT 1")  # Consulta de prueba
        return {"message": "Conexión exitosa a la base de datos"}
    except Exception as e:
        return {"edrror": str(e)}
