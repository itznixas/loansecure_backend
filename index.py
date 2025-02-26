from typing import Union
from fastapi import FastAPI, Depends
from src.config import ConfiguracionDeEnv  # Importa la clase correctamente
from src.database.database import create_db_and_tables, get_session
from sqlmodel import Session  # Asegúrate de importar Session
from typing import Annotated  # Usa typing en lugar de typing_extensions
#from src.routes.user_router import router as user_router
#from src.auth.auth_routes import router as auth_router

import src.models.user_model
import src.models.client_model
import src.models.balances_model  
import src.models.loan_status_model 
import src.models.payments_model
import src.models.loan_model


app = FastAPI()

# Instancia de la clase de configuración
config = ConfiguracionDeEnv()

# Dependencia de sesión
SessionDep = Annotated[Session, Depends(get_session)]  # Ahora Session está importado correctamente

@app.get("/")
def read_root():
    return {"messagde":"Hello, FastAPI with Docker!"}


#app.include_router(user_router)
#app.include_router(auth_router)

@app.on_event("startup")
def on_startup():
    print("🚀 Creando las tablas en la base de datos...")  # ✅ Agrega un print para depuración
    create_db_and_tables()
    print("✅ Tablas creadas exitosamente.")  # ✅ Mensaje de confirmación
 