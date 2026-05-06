"""Modulo para operações no banco de dados."""

import asyncio

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.engine import CursorResult

from src.database.settings import database_connection

Base = declarative_base(metadata=MetaData())


class Database:
    """Classe para operações no banco de dados."""

    engine = create_engine(database_connection.CONN_URL)

    @classmethod
    async def fetch_one(cls, query) -> dict | None:
        """Busca uma linha do banco de dados.

        Args:
            query (): A query a ser executada.

        Returns:
            dict | None: Dicionario se houver alguma linha, None caso contrario.
        """
        cursor = await cls.execute(query)
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
        cursor = await cls.execute(query)
        rows = cursor.fetchall()
        return [(row._mapping) for row in rows]

    @classmethod
    async def execute(cls, query) -> CursorResult:
        """Executa uma query.

        Args:
            query (): A query a ser executada.
        """
        def func(query) -> CursorResult:
            """"Função para executar a query de forma síncrona.
            
            Args:
                query (): A query a ser executada.
            
            Returns:
                CursorResult: O resultado da execução da query.
            """
            with cls.engine.begin() as conn:
                cursor = conn.execute(query)
                return cursor
        return await asyncio.to_thread(func, query)

    @classmethod
    async def execute_many(cls, queries: list) -> None:
        """Executa várias queries em uma transação.

        Args:
            queries (): Lista de queries a serem executadas.
        """
        def func(queries):
            """Executa várias queries em uma transação.

            Args:
                queries (): Lista de queries a serem executadas.
            """
            with cls.engine.begin() as conn:
                for query in queries:
                    conn.execute(query)
        await asyncio.to_thread(func, queries)

    @classmethod
    async def init_models(cls) -> None:
        """Cria todas as tabelas do banco de dados."""
        with cls.engine.begin() as conn:
            Base.metadata.create_all(bind=conn)

    @classmethod
    async def drop_models(cls) -> None:
        """Deletas todas as tabelas do banco de dados."""
        with cls.engine.begin() as conn:
            Base.metadata.drop_all(bind=conn)
