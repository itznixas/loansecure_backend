from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from src.schemas.user_schemas import UserCreateShema, UserResponseSchema
from src.models.user_model import User
from src.database.database import get_session
from src.services.user_service import user_register_service
from sqlmodel import Session

oauth2_scheme = OAuth2PasswordBearer("/auth")

router = APIRouter(prefix="/auth") 


@router.post("/signup", response_model=UserResponseSchema)
async def register(user_data: UserCreateShema, session : Session = Depends(get_session)):
    user = user_register_service(user_data, session)
    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at
    }
   

@router.get("/users/me")
def user(token: str = Depends(oauth2_scheme)):
    print(token)
    return "HELLO"



