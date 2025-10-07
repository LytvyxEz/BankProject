from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

from .routers import user_router, wallet_router


app = FastAPI(debug=True)
app.add_middleware(SessionMiddleware, secret_key="super-secret-key")


app.include_router(user_router)
app.include_router(wallet_router)
