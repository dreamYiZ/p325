from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Good(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)  # specify a length, e.g., 50
    price = Column(Integer)
    discount = Column(Integer)
    kind = Column(String(50))  # specify a length, e.g., 50
    tag = Column(String(50))  # specify a length, e.g., 50
    opts = Column(String(255))  # specify a length, e.g., 255
    img = Column(String(255))  # specify a length, e.g., 255

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    sn = Column(String(50))
    total = Column(Integer)
    goods = Column(JSON)
    created_date = Column(DateTime, default=datetime.utcnow)
    paid_date = Column(DateTime)
    payment_amount = Column(Float)
