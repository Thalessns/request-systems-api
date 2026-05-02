"""Exceções para o módulo de usuários."""

from fastapi import status

from src.app.exceptions import CustomBaseException


class UsuarioNaoEncontradoException(CustomBaseException):
    """Exceção lançada quando um usuário não é encontrado."""

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Usuario com '{campo}' = '{valor}' nao foi encontrado."


class UsuarioJaCadastradoException(CustomBaseException):
    """Exceção lançada quando um usuário já está cadastrado."""

    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Usuario com '{campo}' = '{valor}' ja está cadastrado."


class CredenciaisInvalidasException(CustomBaseException):
    """Exceção lançada quando as credenciais são inválidas."""

    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Credenciais inválidas."
