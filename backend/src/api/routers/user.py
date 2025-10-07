from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from database.crud import create_user, get_users, get_db
from schemas import User, UserRequest, bank
from uttils import try_except

user_router = APIRouter(prefix="/user", tags=["Users"])


@try_except
@user_router.post("/create")
def create_user_route(user_request: UserRequest, db: Session = Depends(get_db)):
    user_data = bank.create_user(
        username=user_request.username,
        email=user_request.email,
        password=user_request.password
    )

    return create_user(user_data, db)




@try_except
@user_router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)
