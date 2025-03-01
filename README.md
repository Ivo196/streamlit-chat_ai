# Streamlit Chat AI with Gemini 1.5

Una aplicación de chat simple construida con Streamlit y la API de Gemini 1.5 de Google.

## Requisitos

- Python 3.10 o superior
- Una API key de Google Gemini

## Configuración

1. Clona este repositorio:
   ```bash
   git clone https://github.com/yourusername/streamlit-chat_ai.git
   cd streamlit-chat_ai
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` basado en `.env.example` y añade tu API key de Gemini:
   ```bash
   cp .env.example .env
   # Edita el archivo .env y añade tu API key
   ```

## Ejecución

### Ejecución local

```bash
streamlit run app/chat_ai_gemini.py
```

La aplicación estará disponible en http://localhost:8501

### Ejecución con Docker

1. Construye la imagen:
   ```bash
   docker build -t streamlit-chat-ai .
   ```

2. Ejecuta el contenedor:
   ```bash
   docker run -p 8501:8501 --env-file .env streamlit-chat-ai
   ```

   > **Nota sobre variables de entorno y Docker**: 
   > - El archivo `.env` no se incluye en la imagen Docker (está en `.dockerignore`).
   > - Al usar `--env-file .env`, Docker lee las variables del archivo y las hace disponibles dentro del contenedor.
   > - La aplicación dentro del contenedor puede acceder a estas variables mediante `os.getenv()`.
   > - Si prefieres no usar un archivo `.env`, también puedes pasar variables individuales con `-e`:
   >   ```bash
   >   docker run -p 8501:8501 -e GEMINI_API=tu_api_key streamlit-chat-ai
   >   ```
   >   Pero esto no es recomendable para secretos, ya que quedarían visibles en el historial de comandos.

La aplicación estará disponible en http://localhost:8501

## Características

- Interfaz de chat simple y amigable
- Integración con el modelo Gemini 1.5 Flash de Google
- Historial de conversación persistente durante la sesión

## Estructura del proyecto

```
streamlit-chat_ai/
├── app/
│   └── chat_ai_gemini.py    # Aplicación principal
├── .dockerignore            # Archivos a ignorar en la imagen Docker
├── .env.example             # Plantilla para variables de entorno
├── Dockerfile               # Configuración para Docker
├── README.md                # Este archivo
└── requirements.txt         # Dependencias del proyecto
```

## Licencia

[MIT](https://choosealicense.com/licenses/mit/) 