"""Modulo para os schemas de usuario."""

from datetime import datetime
from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo, Field

from src.app.exceptions import CampoInvalidoException
from src.app.utils import obter_agora_br
from src.usuarios.senha import SenhaHandler


class UsuarioCriar(BaseModel):
    """Schema base de usuario com campos obrigatórios."""

    nome_usuario: str
    email: EmailStr
    num_matricula: str
    area: str
    cargo: str
    tipo_perfil: str
    status_usuario: str
    senha_hash: str
    criado_por: str
    dt_criacao: datetime = Field(default_factory=obter_agora_br)

    @field_validator("nome_usuario", mode="before")
    def validar_nome(cls, value: str) -> str:
        """Valida se o nome é uma string e não está vazio.

        Args:
            value (str): Valor a ser validado.

        Returns:
            str: Valor validado.

        Raises:
            CampoInvalidoException: Se o nome não tiver pelo menos 3 caracteres.
        """
        if len(value) < 3:
            raise CampoInvalidoException(
                campo="nome_usuario", mensagem="Deve ter pelo menos 3 caracteres."
            )
        return value

    @field_validator("num_matricula", "criado_por", mode="before")
    def validar_matricula(cls, value: str, info: ValidationInfo) -> str:
        """Valida se a matrícula tem exatamente 5 dígitos numéricos.

        Args:
            value (str): Valor a ser validado.
            info (ValidationInfo): Informações sobre o campo sendo validado.

        Returns:
            str: Valor validado.

        Raises:
            CampoInvalidoException: Se a matrícula não contiver apenas números.
            CampoInvalidoException: Se a matrícula não tiver 5 dígitos.
        """
        campo_nome = info.field_name
        if not value.isdigit():
            raise CampoInvalidoException(
                campo=campo_nome, mensagem="Deve conter apenas números."
            )
        if len(value) != 5:
            raise CampoInvalidoException(
                campo=campo_nome, mensagem="Deve ter exatamente 5 dígitos."
            )
        return value

    @field_validator("area", mode="before")
    def validar_area(cls, value: str) -> str:
        """Valida se a area não está vazia.

        Args:
            value (str): Valor a ser validado.

        Returns:
            str: Valor validado.

        Raises:
            CampoInvalidoException: Se a area estiver vazia.
        """
        if not value or len(value.strip()) == 0:
            raise CampoInvalidoException(campo="area", mensagem="Não pode estar vazio.")
        return value

    @field_validator("senha_hash", mode="before")
    def validar_senha(cls, value: str) -> str:
        """Valida se a senha não está vazia.

        Args:
            value (str): Valor a ser validado.

        Returns:
            str: Valor validado.

        Raises:
            CampoInvalidoException: Se a senha estiver vazia.
        """
        if not value or len(value.strip()) == 0:
            raise CampoInvalidoException(
                campo="senha_hash", mensagem="Não pode estar vazio."
            )
        return SenhaHandler.criptografar_senha(value)


class Usuario(BaseModel):
    """Schema completo do usuario (resposta)."""

    nome_usuario: str
    email: EmailStr
    num_matricula: str
    area: str
    cargo: str
    tipo_perfil: str
    status_usuario: str
    senha_hash: str
    criado_por: str
    dt_criacao: datetime
    ultimo_login: datetime | None = None
    atualizado_por: str | None = None
    ultima_atualizacao: datetime | None = None
    status_cadastro: str | None = None


class UsuarioLogin(BaseModel):
    """Schema de login."""

    num_matricula: str | None = None
    email: EmailStr | None = None
    senha: str
