from src.schemas.user_schemas import UserCreateShema
from src.models.user_model import User
from datetime import datetime
from fastapi import Depends
from sqlmodel import Session
from src.auth.pass_hash import hashed_password
from src.database.database import get_session

def user_register_service(user_data: UserCreateShema, session: Session):
    hashed = hashed_password(user_data.password)

    new_user = User(
        username = user_data.username,
        email = user_data.email,
        hashed_password = hashed,
        created_at=datetime.utcnow(),
        disabled= user_data.disabled if user_data.disabled is not None else False  
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
