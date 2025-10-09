from sqlalchemy import DECIMAL, Column, String, Integer, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class WalletOrm(Base):
    __tablename__ = 'wallets'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    card = Column(String, unique=True, nullable=False)
    money = Column(DECIMAL, default=0)
    security_code = Column(Integer, nullable=False)

    user = relationship('UserOrm', back_populates='wallets')
