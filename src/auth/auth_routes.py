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
    user = AuthService.authenticate_user(user_data.email, user_data.password, session)

    
    if not user:
        #log_warning(f"Login failed: Invalid credentials for {user_data.email}")
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token = AuthService.create_access_token(user.email)
    return {"access_token": access_token, "token_type": "bearer"}



@router.get("/user/me")
async def read_user_me(
    token: Annotated[str, Depends(oauth2_scheme)],  # Extrae el token del encabezado
    session: Session = Depends(get_session)
):
    """
    Devuelve la información del usuario autenticado.
    """
    email = verify_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Busca al usuario en la base de datos
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Devuelve la información del usuario
    return {
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at
    }