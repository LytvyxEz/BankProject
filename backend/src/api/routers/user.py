from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from database.crud import create_user, get_users, get_db, get_user, login_user
from schemas import User, UserRequest, bank, UserRequestRegister, UserResponse
from uttils import try_except, staff_only, hash_password, auth_user, not_auth_user


user_router = APIRouter(prefix="/user", tags=["User api"])


@try_except
@user_router.post("/register", response_model=UserResponse)
def register(request: Request, user_request: UserRequestRegister, user=Depends(not_auth_user), db: Session = Depends(get_db)):
    user_data = bank.login_register(
        username=user_request.username,
        email=user_request.email,
        password=user_request.password
    )
    user = create_user(user_data, db)
    return user



@try_except
@user_router.post('/login', response_model=UserResponse)
def login(request: Request, user_request: UserRequest, user=Depends(not_auth_user), db: Session = Depends(get_db)):
    user_data = bank.login_register(
        username=user_request.username,
        email=user_request.email, 
        password=user_request.password
    )
    
    user = login_user(user_data, db)
    request.session['user'] = user.id
    return user



@try_except
@user_router.get('/get_user', response_model=UserResponse)
def get_user_api(request: Request, user=Depends(auth_user), db: Session = Depends(get_db)):
    user_obj = get_user(db, user_id=user)
    return user_obj


@try_except
@user_router.post('/logout')
def logout_user(request: Request, user=Depends(auth_user), db: Session = Depends(get_db)):
    user_obj = user
    request.session['user'] = None
    return {
        'message': 'user is succesfully logged out',
            'user': user_obj
            }


# @try_except
# @user_router.get("/get_all_users")
# @staff_only
# def get_all_users(db: Session = Depends(get_db)):
#     return get_users(db)


