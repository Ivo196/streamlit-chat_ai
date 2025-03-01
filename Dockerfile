# Python Image Official
FROM python:3.10-slim

WORKDIR /app

# Copiar solo los archivos de requisitos primero para aprovechar el caché de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
# Nota: .env no se copiará si está en .dockerignore
COPY . .

# Exponer el puerto de Streamlit
EXPOSE 8501

# RUN APP 
CMD ["streamlit", "run", "app/chat_ai_gemini.py", "--server.port=8501", "--server.address=0.0.0.0" ]