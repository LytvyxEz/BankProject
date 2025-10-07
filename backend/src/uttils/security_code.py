from random import randint
import datetime

from uttils.deco import try_except


@try_except
def create_security_code() -> dict:
    security_code = randint(100, 999)
    expires_at = datetime.datetime.now() + datetime.timedelta(minutes=60)
    expires_in = expires_at - datetime.datetime.now()
    return {"code": security_code, "expires_in": int(expires_in.total_seconds() / 60)}