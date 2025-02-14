from typing import Union
from fastapi import FastAPI, Depends
from config import ConfiguracionDeEnv  # Importa la clase correctamente
from src.database.database import create_db_and_tables, get_session
from sqlmodel import Session  # Asegúrate de importar Session
from typing import Annotated  # Usa typing en lugar de typing_extensions
from src.routes.user_router import router as user_router

app = FastAPI()

# Instancia de la clase de configuración
config = ConfiguracionDeEnv()

# Dependencia de sesión
SessionDep = Annotated[Session, Depends(get_session)]  # Ahora Session está importado correctamente

@app.get("/")
def read_root():
    return {"messagde":"Hello, FastAPI with Docker!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

app.include_router(user_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()  # Ejecuta la creación de tablas en el inicio


