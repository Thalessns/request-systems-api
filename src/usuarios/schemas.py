"""Modulo para os schemas de usuario."""

from pydantic import BaseModel, EmailStr, field_validator

from src.app.exceptions import CampoInvalidoException

class Usuario(BaseModel):
    """Schema de usuario."""

    matricula: str
    nome: str
    email: EmailStr
    equipe: str

    @field_validator("matricula", mode="before")
    def validar_matricula(value: str) -> str:
        """Valida se a matricula é um inteiro.

        Args:
            value (str): Valor a ser validado.

        Returns:
            str: Valor validado.

        Raises:
            CampoInvalidoException: Se a matricula não for um inteiro.
            CampoInvalidoException: Se a matricula não tiver 5 digitos.
        """
        if not value.isdigit():
            raise CampoInvalidoException(campo="matricula", mensagem="Deve conter apenas números.")
        if len(value) != 5:
            raise CampoInvalidoException(campo="matricula", mensagem="Deve ter 5 digitos.")
        return value

    @field_validator("nome", mode="before")
    def validar_nome(value: str) -> str:
        """Valida se o nome é uma string e não está vazio.

        Args:
            value (str): Valor a ser validado.

        Returns:
            str: Valor validado.

        Raises:
            CampoInvalidoException: Se o nome não for uma string.
            CampoInvalidoException: Se o nome não tiver pelo menos 3 letras.
        """
        if not value.isalpha():
            raise CampoInvalidoException(campo="nome", mensagem="Deve conter apenas letras.")
        if len(value) < 3:
            raise CampoInvalidoException(campo="nome", mensagem="Deve ter pelo menos 3 letras.")
        return value

    @field_validator("equipe", mode="before")
    def validar_equipe(value: str) -> str:
        """Valida se a equipe é uma string e é válida.

        Args:
            value (str): Valor a ser validado.

        Returns:
            str: Valor validado.

        Raises:
            CampoInvalidoException: Se a equipe não for uma string.
            CampoInvalidoException: Se a equipe não tiver pelo menos uma letra.
        """
        if not value.isalpha():
            raise CampoInvalidoException(campo="equipe", mensagem="Deve conter apenas letras.")
        if len(value) == 0:
            raise CampoInvalidoException(campo="equipe", mensagem="Deve ter pelo menos uma letra.")
        return value
