from pydantic import EmailStr, BaseModel, Field, field_validator, model_validator
from fastapi import HTTPException
from string import punctuation

from uttils import try_except, hash_password


special_chars = punctuation


class User:
    @try_except
    def __init__(self, username: str, email: EmailStr, password: str, wallet=None):
        self.username = username
        self.email = email
        self.password = hash_password(password)
        self.wallet = wallet if wallet else 'You need to create a wallet to see it'
        
        
        
    @staticmethod
    @try_except
    def create_user(username: str, email: EmailStr, password: str):
        return User(username, email, password)
    
    @try_except
    def __str__(self) -> str:
        return f"username: {self.username}\nemail: {self.email}\npassword: {self.password}\n{self.wallet}"  
        
        
    
    
class UserRequest(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr = Field()
    password: str = Field(min_length=8)
    
    
class UserRequestRegister(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=8)
    password2: str = Field(min_length=8)

    @model_validator(mode='after')
    def check_passwords_match(self):
        if self.password != self.password2:
            raise ValueError("Passwords do not match")
        return self
    
    @field_validator('password')
    def validate_password(cls, value: str):
        if not any(char.isupper() for char in value):
            raise HTTPException(400, "Password must have at least one uppercase letter")

        if not any(char.islower() for char in value):
            raise HTTPException(400, "Password must have at least one lowercase letter")

        if not any(char.isdigit() for char in value):
            raise HTTPException(400, "Password must have at least one digit")

        if not any(char in special_chars for char in value):
            raise HTTPException(400, "Password must have at least one special symbol")

        return value
            


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True 

    