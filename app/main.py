import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

from routes.client import router as client_router



app = FastAPI()

# Configurando o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Especificar a origem permitida
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["*"],  # Cabeçalhos permitidos
)

# Incluindo os roteadores
app.include_router(client_router)



# Endpoint de teste


@app.get('/')
def test_api():
    return {"mensage": "API rodando!"}

# Executando o servidor
if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000,
                            host='0.0.0.0', log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()