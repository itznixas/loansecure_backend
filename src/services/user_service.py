from src.schemas.user_schemas import UserCreateShema
from src.models.user_model import User
from datetime import datetime
from fastapi import HTTPException
from sqlmodel import Session
from src.auth.pass_hash import hashed_password 
from src.database.database import get_session
from src.utils.validation.validation_user import validate_email, validate_password, validate_username
  
def user_register_service(user_data: UserCreateShema, session: Session):
    
    is_valid, message = validate_password(user_data.password)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message) 
        
    validate_email(user_data, session)
    validate_username(user_data, session)

    hashed = hashed_password(user_data.password)

    new_user = User(
        username=user_data.username,
        email=user_data.email, 
        hashed_password=hashed,
        created_at=datetime.utcnow(),
        disabled=user_data.disabled if user_data.disabled is not None else False  
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
