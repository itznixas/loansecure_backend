from dotenv import load_dotenv

import os

load_dotenv();

class ConfiguracionDeEnv:
    SECRET_KEY = os.getenv("SECRET_KEY")