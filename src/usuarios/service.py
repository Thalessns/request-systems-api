"""Modulo para serviços de usuários."""

from sqlalchemy.exc import IntegrityError

from src.database.database import Database
from src.usuarios.entity import tabela_usuarios
from src.usuarios.schemas import Usuario
from src.usuarios.exceptions import (
    UsuarioNaoEncontradoException,
    UsuarioJaCadastradoException
)

class UsuarioService:
    """Serviços de usuários."""

    @classmethod
    async def criar_usuario(cls, user: Usuario) -> Usuario:
        """Cria um novo usuário.

        Args:
            user (Usuario): Usuário a ser criado.

        Returns:
            Usuario: Usuário criado.

        Raises:
            UsuarioJaCadastradoException: Se o usuário já for cadastrado.
        """
        try:
            query = tabela_usuarios.insert().values(**user.model_dump())
            await Database.execute(query)
        except IntegrityError as error:
            msg = str(error.orig)
            if "usuarios.email" in msg:
                raise UsuarioJaCadastradoException(campo="email", valor=user.email)
            elif "usuarios.matricula" in msg:
                raise UsuarioJaCadastradoException(campo="matricula", valor=user.matricula)
        return user

    @classmethod
    async def buscar_usuarios(cls) -> list[Usuario]:
        """Busca todos os usuários.

        Returns:
            list[Usuario]: Lista de usuários.
        """
        query = tabela_usuarios.select()
        return [Usuario(**user) for user in await Database.fetch_all(query)]

    @classmethod
    async def buscar_usuario_email(cls, email: str) -> Usuario:
        """Busca um usuário por email.

        Args:
            email (str): Email do usuário a ser buscado.

        Returns:
            Usuario: Usuário encontrado.

        Raises:
            UsuarioNaoEncontradoException: Se o usuário não for encontrado.
        """
        query = tabela_usuarios.select().where(tabela_usuarios.c.email == email)
        usuario = await Database.fetch_one(query)
        if not usuario:
            raise UsuarioNaoEncontradoException(campo="email", valor=email)
        return Usuario(**usuario)
    
    @classmethod
    async def buscar_usuario_matricula(cls, matricula: str) -> Usuario:
        """Busca um usuário por matricula.

        Args:
            matricula (str): Matricula do usuário a ser buscado.

        Returns:
            Usuario: Usuário encontrado.

        Raises:
            UsuarioNaoEncontradoException: Se o usuário não for encontrado.
        """
        query = tabela_usuarios.select().where(tabela_usuarios.c.matricula == matricula)
        usuario = await Database.fetch_one(query)
        if not usuario:
            raise UsuarioNaoEncontradoException(campo="matricula", valor=matricula)
        return Usuario(**usuario)
