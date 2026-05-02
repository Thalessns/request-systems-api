"""Utilitários gerais da aplicação."""

from datetime import datetime, UTC, timezone, timedelta

# Fuso horário do Brasil (Horário de Brasília, UTC-3)
TZ_BR = timezone(timedelta(hours=-3), name="America/Sao_Paulo")


def obter_agora_br() -> datetime:
    """Retorna a data e hora atual no fuso horário do Brasil."""
    return datetime.now(TZ_BR)


def obter_agora_utc() -> datetime:
    """Retorna a data e hora atual em UTC."""
    return datetime.now(UTC)
