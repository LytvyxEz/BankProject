from bcrypt import hashpw, checkpw, gensalt

from uttils.deco import try_except

@try_except
def hash_password(password: str) -> str:
    return hashpw(password.encode(), gensalt(rounds=12)).decode()