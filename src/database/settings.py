"""Modulo de configurações do banco de dados."""

from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    """Classe para configuração do banco de dados."""

    CONN_URL: str = "sqlite+aiosqlite:///src/database/data/db.sql"


database_settings = DatabaseSettings()
