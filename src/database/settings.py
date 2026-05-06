"""Modulo de configurações do banco de dados."""

from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    """Classe para configuração do banco de dados."""

    DATABRICKS_TOKEN: str = "Your Databricks Token"
    DATABRICKS_HOST: str = "Your Databricks Host"
    DATABRICKS_HTTP_PATH: str = "Your Databricks HTTP Path"
    DATABRICKS_CATALOG: str = "Your Databricks Catalog"
    DATABRICKS_SCHEMA: str = "Your Databricks Schema"


database_settings = DatabaseSettings()


class DatabaseConnection:
    """Classe para configuação da conexão com o banco de dados."""

    CONN_URL: str = (
        f"databricks://token:{database_settings.DATABRICKS_TOKEN}@{database_settings.DATABRICKS_HOST}?"
        f"http_path={database_settings.DATABRICKS_HTTP_PATH}&catalog={database_settings.DATABRICKS_CATALOG}&schema={database_settings.DATABRICKS_SCHEMA}"
    )


database_connection = DatabaseConnection()
