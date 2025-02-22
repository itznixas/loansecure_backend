from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.database.database import get_session
from src.models.userModel import User
from src.schemas.user_schemas import UserCreateShema, UserResponseSchema
from src.services.user_service import user_register_service

router = APIRouter(prefix="/users") 

@router.post("/register", response_model=UserCreateShema)
def user_register_route(user_data: UserCreateShema, session: Session = Depends(get_session)):
    
    user = user_register_service(user_data, session)
    
    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at
    }
   



@router.get("/test-db")
def test_db_connection():
    try:
        with Session(engine) as session:
            session.exec(text("SELECT 1"))  # ✅ Ahora es válido
        return {"message": "Conexión exitosa a la base de datos"}
    except Exception as e:
        return {"error": str(e)}



