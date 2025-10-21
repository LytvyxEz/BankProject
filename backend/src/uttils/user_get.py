from fastapi import HTTPException, status, Request

def auth_user(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return user


def not_auth_user(request: Request):
    user = request.session.get("user")
    if user:
        raise HTTPException(
            status_code=400,
            detail="User already exists",
        )
    return user
