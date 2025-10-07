from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import User_orm
from schemas import UserRequest

from .session import get_db


def create_user(user_data: dict, db: Session):
    db_user = db.query(User_orm).filter(User_orm.email == user_data["email"]).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User_orm(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(User_orm).all()
