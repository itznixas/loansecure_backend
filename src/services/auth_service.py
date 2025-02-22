from sqlmodel import Session, select
from fastapi import HTTPException, status

from src.models.user_model import User
from src.auth.pass_hash import verify_password
from src.auth.jwt_handler import create_access_token, verify_token


class AuthService:
    @staticmethod
    def authenticate_user(email: str, password: str, session: Session):
        user = session.exec(select(User).where(User.email == email)).first()
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def create_access_token(email: str):
        return create_access_token({"sub": email})

    @staticmethod
    def get_current_user(token: str, session: Session):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        email = verify_token(token)
        if not email:
            raise credentials_exception

        user = session.exec(select(User).where(User.email == email)).first()
        if not user:
            raise credentials_exception

        return user
