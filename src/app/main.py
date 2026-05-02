"""Arquivo principal da API."""

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database.database import Database
from src.usuarios.router import usuario_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context for the application."""
    await Database.init_models()
    yield


app = FastAPI(
    title="Request Systems API", version="0.1.0", prefix="/api", lifespan=lifespan
)


@app.get("/")
def read_root():
    """Root endpoint.

    Returns:
        dict: Mensagem de boas-vindas.
    """
    return {"message": "Welcome to Request Systems API!"}


app.include_router(usuario_router)
