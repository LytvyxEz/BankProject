from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import UserOrm
from schemas import UserRequest

from .session import get_db
from uttils import verify_password


def create_user(user_data: dict, db: Session):
    db_user = db.query(UserOrm).filter(UserOrm.email == user_data["email"]).first()
    db_user2 = db.query(UserOrm).filter(UserOrm.username == user_data["username"]).first()

    if db_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    if db_user2:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    new_user = UserOrm(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user(user_data: dict, db: Session):
    db_user = db.query(UserOrm).filter(UserOrm.email == user_data["email"]).first()
    
    if not db_user:
        raise HTTPException(status_code=400, detail='User does not exists')

    if not verify_password(user_data['password'], db_user.password):
        raise HTTPException(status_code=400, detail='Invalid password')        
        
    return db_user


def get_users(db: Session):
    return db.query(UserOrm).all()

def get_user(db: Session, user_id):
    if not user_id:
        raise HTTPException(status_code=401, detail='User is not authtentificated')
    user_obj = db.query(UserOrm).filter_by(id=user_id).first()
    if not user_obj:
        raise HTTPException(status_code=401, detail="User does not exists")
    return user_obj

