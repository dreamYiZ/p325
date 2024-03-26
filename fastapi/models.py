from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
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



class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    good_id = Column(Integer, ForeignKey("goods.id"))
    count = Column(Integer)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    sn = Column(String(50))
    total = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    items = relationship("OrderItem", backref="order")
