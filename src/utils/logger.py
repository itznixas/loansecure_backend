import logging

# Configuración del logger
logging.basicConfig(
    filename="app.log",  # Archivo donde se guardarán los logs
    level=logging.INFO,  # Nivel mínimo de logs a registrar
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato del log
    datefmt="%Y-%m-%d %H:%M:%S",  # Formato de fecha
)

# Funciones de logging para eventos específicos
def login_success(username):
    logging.info(f"Usuario '{username}' ha iniciado sesión exitosamente.")

def login_failed(username):
    logging.warning(f"Intento de inicio de sesión fallido para usuario '{username}'.")

def register_success(username):
    logging.info(f"Nuevo usuario registrado: '{username}'.")

