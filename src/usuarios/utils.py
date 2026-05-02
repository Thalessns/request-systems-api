"""Utilitários para usuários."""

from src.usuarios.exceptions import UsuarioNaoEncontradoException
from src.usuarios.schemas import UsuarioCriar
from src.usuarios.service import UsuarioService


async def criar_admin() -> None:
    """Cria o admin."""
    admin = UsuarioCriar(
        nome_usuario="admin",
        senha_hash="1",
        cargo="Administrador",
        tipo_perfil="Admin",
        area="TI",
        num_matricula="99999",
        status_usuario="Ativo",
        email="admin@dominio.com",
        criado_por="00000",
    )
    try:
        await UsuarioService.buscar_usuario_matricula("99999")
    except UsuarioNaoEncontradoException:
        await UsuarioService.criar_usuario(admin)
    
    