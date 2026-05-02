"""Modulo para serviços de usuários."""

from sqlalchemy.exc import IntegrityError

from src.database.database import Database
from src.usuarios.entity import tabela_usuarios
from src.usuarios.schemas import (
    Usuario,
    UsuarioCriar,
    UsuarioLogin,
)
from src.usuarios.exceptions import (
    UsuarioNaoEncontradoException,
    UsuarioJaCadastradoException,
    CredenciaisInvalidasException,
)
from src.usuarios.senha import SenhaHandler
from src.app.utils import obter_agora_br


class UsuarioService:
    """Serviços de usuários."""

    @classmethod
    async def criar_usuario(cls, user: UsuarioCriar) -> Usuario:
        """Cria um novo usuário.

        Args:
            user (UsuarioCriar): Usuário a ser criado.

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
            elif "usuarios.num_matricula" in msg:
                raise UsuarioJaCadastradoException(
                    campo="num_matricula", valor=user.num_matricula
                )
        return Usuario(**user.model_dump())

    @classmethod
    async def login(cls, dados: UsuarioLogin) -> None:
        """Realiza o login do usuário.

        Args:
            dados (UsuarioLogin): Dados do usuário a ser logado.


        """
        query = tabela_usuarios.select()
        campo = ""
        if dados.num_matricula:
            campo = "matricula"
            query = query.where(tabela_usuarios.c.num_matricula == dados.num_matricula)
        elif dados.email:
            campo = "email"
            query = query.where(tabela_usuarios.c.email == dados.email)
        if campo == "":
            raise CredenciaisInvalidasException()

        usuario = await Database.fetch_one(query)
        if not usuario:
            raise CredenciaisInvalidasException()
        if not SenhaHandler.verificar_senha(dados.senha, usuario.get("senha_hash")):
            raise CredenciaisInvalidasException()

        query_update = (
            tabela_usuarios.update()
            .where(tabela_usuarios.c.num_matricula == usuario.get("num_matricula"))
            .values(ultimo_login=obter_agora_br())
        )
        await Database.execute(query_update)

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
    async def buscar_usuario_matricula(cls, num_matricula: str) -> Usuario:
        """Busca um usuário por matricula.

        Args:
            num_matricula (int): Matricula do usuário a ser buscado.

        Returns:
            Usuario: Usuário encontrado.

        Raises:
            UsuarioNaoEncontradoException: Se o usuário não for encontrado.
        """
        query = tabela_usuarios.select().where(
            tabela_usuarios.c.num_matricula == num_matricula
        )
        usuario = await Database.fetch_one(query)
        if not usuario:
            raise UsuarioNaoEncontradoException(
                campo="num_matricula", valor=num_matricula
            )
        return Usuario(**usuario)
