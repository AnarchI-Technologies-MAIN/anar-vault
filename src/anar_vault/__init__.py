"""Canonical secrets and encrypted-storage infrastructure for AnarchI."""

from .vault import SecretVaultError, read_vault, write_vault

__all__ = [
    "SecretVaultError",
    "read_vault",
    "write_vault",
]