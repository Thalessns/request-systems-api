"""Modulo de rotas de usuários."""

from fastapi import APIRouter, status

from src.usuarios.schemas import Usuario, UsuarioAtualizar, UsuarioCriar, UsuarioLogin
from src.usuarios.service import UsuarioService

usuario_router = APIRouter(prefix="/usuarios")


@usuario_router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_usuario(usuario: UsuarioCriar) -> Usuario:
    """Endpoint de criação de usuário.

    Args:
        usuario (UsuarioCriar): Usuário a ser criado.

    Returns:
        Usuario: Usuário criado.
    """
    return await UsuarioService.criar_usuario(usuario)


@usuario_router.put("/{num_matricula}", status_code=status.HTTP_200_OK)
async def atualizar_usuario(num_matricula: str, dados: UsuarioAtualizar) -> Usuario:
    """Endpoint de atualização de usuário.

    Args:
        num_matricula (str): Matrícula do usuário a ser atualizado.
        dados (UsuarioAtualizar): Dados a serem atualizados.

    Returns:
        Usuario: Usuário atualizado.
    """
    return await UsuarioService.atualizar_usuario(num_matricula, dados)


@usuario_router.put("/login", status_code=status.HTTP_200_OK)
async def login(dados: UsuarioLogin):
    """Endpoint de login de usuário.

    Args:
        dados (UsuarioLogin): Usuário a ser logado.
    """
    await UsuarioService.login(dados)


@usuario_router.get("/", status_code=status.HTTP_200_OK)
async def buscar_usuarios() -> list[Usuario]:
    """Endpoint de busca de usuários.

    Returns:
        list[Usuario]: Lista de usuários.
    """
    return await UsuarioService.buscar_usuarios()


@usuario_router.get("/email", status_code=status.HTTP_200_OK)
async def buscar_usuario_email(email: str) -> Usuario:
    """Endpoint de busca de usuário por email.

    Args:
        email (str): Email do usuário a ser buscado.

    Returns:
        Usuario: Usuário encontrado.
    """
    return await UsuarioService.buscar_usuario_email(email)


@usuario_router.get("/matricula", status_code=status.HTTP_200_OK)
async def buscar_usuario_matricula(num_matricula: str) -> Usuario:
    """Endpoint de busca de usuário por matricula.

    Args:
        num_matricula (int): Matricula do usuário a ser buscado.

    Returns:
        Usuario: Usuário encontrado.
    """
    return await UsuarioService.buscar_usuario_matricula(num_matricula)
