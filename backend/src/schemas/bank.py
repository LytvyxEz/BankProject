from pydantic import EmailStr

from schemas.enums import Card_enum 
from schemas.user import User
from schemas.wallet import Wallet
from uttils.deco import try_except

class Bank:
    @try_except
    def __init__(self):
        pass    
    
    
    @staticmethod
    @try_except
    def create_wallet(user: User, name: str, card: Card_enum) -> Wallet:
        return Wallet.create_wallet(user, name, card)
    
    @staticmethod
    @try_except
    def create_user(username: str, email: EmailStr, password: str) -> dict:
        user = User.create_user(username, email, password)
        return {
            "username": user.username,
            "email": user.email,
            "password": user.password
        }


    
    @try_except
    def deposit():
        ...
        
    @try_except
    def withdraw():
        ...
        
        
bank = Bank()