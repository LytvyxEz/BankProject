from bcrypt import hashpw, checkpw, gensalt

from .try_except_deco import try_except


@try_except
def hash_password(password: str) -> bytes:
    return hashpw(password.encode(), gensalt(rounds=12))


@try_except
def verify_password(password: str, hashed_password: bytes) -> bool:
    return checkpw(password.encode(), hashed_password)
