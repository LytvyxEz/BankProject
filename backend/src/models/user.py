from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base
from sqlalchemy.orm import relationship

class UserOrm(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(LargeBinary, unique=True, index=True)

    wallets = relationship('WalletOrm', back_populates='user')
