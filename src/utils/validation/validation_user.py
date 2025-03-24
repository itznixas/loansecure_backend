from fastapi import HTTPException
from sqlalchemy import select
from src.models.user_model import User
from src.schemas.user_schemas import UserEmailValidateSchema, UserUsernameValidateSchema
from sqlmodel import Session
import re

def validate_password(password):
    # Patrón: mínimo 8 caracteres, 1 mayúscula, 1 minúscula, 1 número, 1 carácter especial
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    if re.match(patron, password):
        return True, "exito"
    else:
        return False, "The password must have: minimum 8 characters, 1 upper case, 1 lower case, 1 number and 1 special character."  


def validate_email(user_data: UserEmailValidateSchema, session: Session):
    existing_email = session.execute(
        select(User).where(User.email == user_data.email)
    ).scalar_one_or_none()
 
    if existing_email:
        raise HTTPException(status_code=400, detail="the email already this registred")
 

def validate_username(user_data: UserUsernameValidateSchema, session: Session):
    existing_username = session.execute(
        select(User).where(User.username == user_data.username)
    ).scalar_one_or_none()

    if existing_username:
        raise HTTPException(status_code=400, detail="the username already this registred")