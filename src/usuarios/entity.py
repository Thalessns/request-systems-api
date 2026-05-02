"""Modulo para definição da tabela de usuário."""

from sqlalchemy import Column, Integer, String

from src.database.database import Base


class Usuarios(Base):
    """Tabela de usuários."""

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    matricula = Column(String(5), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    equipe = Column(String(50), nullable=False)


tabela_usuarios = Usuarios.__table__
