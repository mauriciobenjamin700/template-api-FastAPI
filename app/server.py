from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints.user import router as user_router

app = FastAPI(
    title="Template de API com FastAPI",
    summary="Um modelo de API com FastAPI",
    description="Um modelo de API com FastAPI para ajudar pessoas a começar a desenvolver suas APIs de forma organizada",
    version="0.0.1",
)

# Configurando o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Especificar a origem permitida
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["*"],  # Cabeçalhos permitidos
)

# Incluindo os roteadores
app.include_router(user_router)


# Endpoint de teste

@app.get('/')
def test_api():
    return {"mensage": "API rodando!"}
