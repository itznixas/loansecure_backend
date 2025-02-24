from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from src.schemas.user_schemas import UserCreateShema, UserResponseSchema, UserLoginSchema
from src.models.user_model import User
from src.database.database import get_session
from src.services.user_service import user_register_service
from sqlmodel import Session, select
from src.auth.jwt_handler import create_access_token, verify_token
from src.auth.pass_hash import verify_password
from src.services.auth_service import AuthService
from typing import Annotated
from src.utils.logger import logging
import time

oauth2_scheme = OAuth2PasswordBearer("/auth")

router = APIRouter(prefix="/auth") 


@router.post("/signup", response_model=UserResponseSchema, status_code=201)
async def register(user_data: UserCreateShema, session : Session = Depends(get_session)):
    user = user_register_service(user_data, session)
    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at,
        "disable": user.disabled
    }
   

@router.post("/login")
def login(user_data: UserLoginSchema, session: Session = Depends(get_session)):
    try:
        user = AuthService.authenticate_user(user_data.email, user_data.password, session)

        access_token = AuthService.create_access_token(user.email)
        logging.info(f"Login successful: User {user.email} logged in")

        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        logging.error(f"Unexpected error during login: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/user/me")
async def read_user_me(
    token: Annotated[str, Depends(oauth2_scheme)],  # Extrae el token del encabezado
    session: Session = Depends(get_session)
):
    email = verify_token(token)
    if not email:
        logging.warning(f"Intento de acceso con token inválido")
        raise HTTPException(status_code=401, detail="Invalid token")

    # Busca al usuario en la base de datos
    user = AuthService.get_current_user(token, session)
    if not user:
        logging.warning(f"Usuario no encontrado para el token proporcionado")
        raise HTTPException(status_code=404, detail="User not found")

    logging.info(f"User '{user.username}' (ID: {user.id}) accedió a su perfil")
    
    return {
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at
    }