import hashlib


def sha256(data) -> str:
    """
    Shortcut for creating SHA256 from Hashlib
    """
    return f"0x{hashlib.sha256(data).hexdigest()}"
