"""Exceções para a API."""

from fastapi import HTTPException, status


class CustomBaseException(HTTPException):
    """Exceção base para a API."""

    STATUS_CODE: int
    DETAIL: str

    def __init__(self, **kwargs: dict[str, any]) -> None:
        """Inicializa a classe."""

        super().__init__(
            status_code=self.STATUS_CODE, detail=self.DETAIL.format(**kwargs)
        )


class CampoInvalidoException(CustomBaseException):
    """Exceção lançada quando um campo é inválido."""

    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Campo '{campo}' inválido. {mensagem}"
