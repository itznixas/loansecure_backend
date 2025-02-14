# Usar la imagen base de Python 3.12 slim
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos al contenedor
COPY requirements.txt .

# Actualizar pip e instalar las dependencias
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente al contenedor
COPY . .

# Configurar variables de entorno
COPY .env .

# Exponer el puerto 8000 para la aplicación FastAPI
EXPOSE 8000

# Comando para iniciar la aplicación con Uvicorn
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "5050",  "--reload"]
