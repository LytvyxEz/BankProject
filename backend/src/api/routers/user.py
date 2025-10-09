from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from database.crud import create_user, get_users, get_db, get_user, login_user
from schemas import User, UserRequest, bank, UserRequestRegister
from uttils import try_except, staff_only, auth_check, hash_password


user_router = APIRouter(prefix="/user", tags=["User api"])


@try_except
@user_router.post("/register")
def register(user_request: UserRequestRegister, db: Session = Depends(get_db)):
    user_data = bank.login_register(
        username=user_request.username,
        email=user_request.email,
        password=user_request.password
    )

    return create_user(user_data, db)


@try_except
@user_router.post('/login')
def login(user_request: UserRequest, db: Session = Depends(get_db)):
    user_data = bank.login_register(
        username=user_request.username,
        email=user_request.email,
        password=user_request.password
    )
    
    user = login_user(user_data, db)
    return user


# @try_except
# @auth_check
# @user_router.get('/get_user')
# def get_user_api(request: Request, db: Session = Depends(get_db)):
#     user = 
#     return get_user(db, user_id=user.id)


@try_except
@staff_only
@user_router.get("/get_all_users")
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)


