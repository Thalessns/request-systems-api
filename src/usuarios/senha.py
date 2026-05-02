"""Utilitários de senha."""

from pwdlib import PasswordHash


class SenhaHandler:
    """Classe utilitária para manipulação de hash de senha."""

    password_hasher = PasswordHash.recommended()

    @classmethod
    def criptografar_senha(cls, senha: str) -> str:
        """Criptografa uma senha.

        Args:
            senha (str): Senha a ser hasheada.

        Returns:
            str: Senha hashada.
        """
        return cls.password_hasher.hash(senha)

    @classmethod
    def verificar_senha(cls, senha: str, senha_hasheada: str) -> bool:
        """Verifica se uma senha é correta.

        Args:
            senha (str): Senha a ser verificada.
            senha_hasheada (str): Hash da senha a ser comparada.

        Returns:
            bool: True se a senha estiver correta, False caso contrario.
        """
        return cls.password_hasher.verify(senha, senha_hasheada)