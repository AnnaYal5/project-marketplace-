from collections import Counter
from typing import List

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(16), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    joined_at = Column(DateTime(timezone=True), server_default=func.now())
    orders: Mapped[List["Order"]] = relationship(back_populates="buyer")
    products: Mapped[List['Product']] = relationship(back_populates='seller')

class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    buyer_id = Column(ForeignKey("user.id"))
    buyer: Mapped["User"] = relationship(back_populates="orders")

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    description = Column(String(512), nullable=False)
    seller_id = Column(ForeignKey('user.id'))
    seller: Mapped['User'] = relationship(back_populates='products')

