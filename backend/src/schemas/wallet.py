from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr
import datetime

from schemas.enums import Card_enum
from uttils.try_except_deco import try_except
from schemas.user import User
from uttils.security_code import create_security_code
        


class Wallet:
    @try_except
    def __init__(self, user: User, name: str, card: Card_enum, money: Decimal = 0):
        self.user = user 
        self.name = name
        self.card = card
        self.money = money
        self.security_code = create_security_code()
        self.user.wallet = self
            
    @try_except
    def generate_new_code(self) -> dict:
        if self.security_code['expires_at'] < datetime.datetime.now():
            self.security_code['expires_at'] =  datetime.datetime.now() + datetime.timedelta(minutes=60)
        return self.security_code
    
    @staticmethod
    @try_except
    def create_wallet(user: User, name: str, card: Card_enum) -> "Wallet":
        return Wallet(user, name, card)
    
    @try_except
    def __str__(self) -> str:
        return f"wallet: {self.name}\ncard: {self.card.value}\nmoney: {self.money}\nsecurity_code: {self.security_code}"
    
    
class CreateWalletRequest(BaseModel):
    user: str #TODO
    name: str
    card: Card_enum


class WalletResponse(BaseModel):
    name: str
    card: str
    money: Decimal
    security_code: dict