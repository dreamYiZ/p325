from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base



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
