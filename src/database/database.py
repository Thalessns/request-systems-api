"""Modulo para operações no banco de dados."""

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

from src.database.settings import database_settings

Base = declarative_base(metadata=MetaData())


class Database:
    """Classe para operações no banco de dados."""

    engine = create_async_engine(database_settings.CONN_URL)

    @classmethod
    async def fetch_one(cls, query) -> dict | None:
        """Busca uma linha do banco de dados.

        Args:
            query (): A query a ser executada.

        Returns:
            dict | None: Dicionario se houver alguma linha, None caso contrario.
        """
        async with cls.engine.connect() as conn:
            cursor = await conn.execute(query)
            row = cursor.fetchone()
            return (row._mapping) if row else None

    @classmethod
    async def fetch_all(cls, query) -> list[dict]:
        """Busca várias linhas do banco de dados.

        Args:
            query (): A query a ser executada.

        Returns:
            list[dict]: Lista de dicionarios se houver alguma linha.
        """
        async with cls.engine.connect() as conn:
            cursor = await conn.execute(query)
            rows = cursor.fetchall()
            return [(row._mapping) for row in rows]

    @classmethod
    async def execute(cls, query) -> None:
        """Executa uma query.

        Args:
            query (): A query a ser executada.
        """
        async with cls.engine.begin() as conn:
            await conn.execute(query)

    @classmethod
    async def execute_many(cls, queries: list) -> None:
        """Executa várias queries em uma transação.

        Args:
            queries (): Lista de queries a serem executadas.
        """
        async with cls.engine.begin() as conn:
            for query in queries:
                await conn.execute(query)

    @classmethod
    async def init_models(cls) -> None:
        """Cria todas as tabelas do banco de dados."""
        async with cls.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @classmethod
    async def drop_models(cls) -> None:
        """Deletas todas as tabelas do banco de dados."""
        async with cls.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
