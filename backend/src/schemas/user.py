from pydantic import EmailStr, BaseModel, Field

from uttils import try_except, hash_password

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
    password: str = Field()