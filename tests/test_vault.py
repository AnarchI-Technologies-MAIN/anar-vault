from __future__ import annotations

from pathlib import Path

from anar_vault import SecretVaultError, read_vault, write_vault


def test_public_contract_is_importable() -> None:
    assert issubclass(SecretVaultError, Exception)
    assert callable(read_vault)
    assert callable(write_vault)


def test_encrypted_round_trip(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("CERBERUS_PIN", "2468")

    path = tmp_path / "memory.vault.json"
    payload = {
        "type": "test.payload",
        "message": "vault round trip",
        "count": 3,
    }

    written = write_vault(
        path,
        payload,
        purpose="anarchi.vault.test",
    )

    assert Path(written).exists()
    assert read_vault(path) == payload