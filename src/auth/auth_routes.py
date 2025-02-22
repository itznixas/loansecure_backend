from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException

oauth2_scheme = OAuth2PasswordBearer("/token")

router = APIRouter() 

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
}

def authenticate_user(db, username, password):
    return ""


@router.get("/users/me")
def user(token: str = Depends(oauth2_scheme)):
    print(token)
    return "HELLO"


@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username, form_data.password)  
    return {"access_token": "ARMADITO", "token_type": "bearer"}
   
