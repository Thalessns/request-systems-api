"""Modulo para definição da tabela de usuário."""

from sqlalchemy import Column, String, DateTime, ForeignKey

from src.database.database import Base
from src.app.utils import obter_agora_br


class Usuarios(Base):
    """Tabela de usuários."""

    __tablename__ = "usuarios"

<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
    id = Column(Integer, primary_key=True, autoincrement=True)
    matricula = Column(String(5), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    equipe = Column(String(50), nullable=False)
=======
>>>>>>> Stashed changes
    nome_usuario = Column(String, nullable=False)
    email = Column(String, nullable=False)
    num_matricula = Column(String(5), primary_key=True)
    area = Column(String, nullable=False)
    cargo = Column(String, nullable=False)
    tipo_perfil = Column(String, nullable=False)
    status_usuario = Column(String, nullable=False)
    senha_hash = Column(String, nullable=False)
    ultimo_login = Column(DateTime, nullable=True)
    dt_criacao = Column(DateTime, nullable=False, default=obter_agora_br)
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
<<<<<<< Updated upstream
    status_cadastro = Column(String, nullable=True)
=======
    ultima_atualizacao = Column(DateTime, nullable=True)
    status_cadastro = Column(String, default="Pendente", nullable=False)
>>>>>>> Stashed changes
>>>>>>> Stashed changes


tabela_usuarios = Usuarios.__table__
