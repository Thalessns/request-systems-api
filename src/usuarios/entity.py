"""Modulo para definição da tabela de usuário."""

from datetime import datetime, UTC
from sqlalchemy import Column, String, DateTime, ForeignKey

from src.database.database import Base


class Usuarios(Base):
    """Tabela de usuários."""

    __tablename__ = "usuarios"

    nome_usuario = Column(String, nullable=False)
    email = Column(String, nullable=False)
    num_matricula = Column(String(5), primary_key=True)
    area = Column(String, nullable=False)
    cargo = Column(String, nullable=False)
    tipo_perfil = Column(String, nullable=False)
    status_usuario = Column(String, nullable=False)
    senha_hash = Column(String, nullable=False)
    ultimo_login = Column(DateTime, nullable=True)
    dt_criacao = Column(DateTime, nullable=False, default=datetime.now(UTC))
    criado_por = Column(
        String(5),
        ForeignKey("usuarios.num_matricula"),
        nullable=False,
    )
    atualizado_por = Column(
        String(5),
        ForeignKey("usuarios.num_matricula"),
        nullable=True,
    )
    status_cadastro = Column(String, nullable=True)


tabela_usuarios = Usuarios.__table__
