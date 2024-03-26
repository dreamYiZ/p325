from pydantic import BaseModel
from typing import List

class GoodBase(BaseModel):
    name: str
    price: int
    discount: int
    kind: str
    tag: str
    opts: str
    img: str

class GoodCreate(GoodBase):
    pass

class GoodInDB(GoodBase):
    id: int

class OrderItemBase(BaseModel):
    good_id: int
    count: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemInDB(OrderItemBase):
    id: int

class OrderBase(BaseModel):
    sn: str
    total: int

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderInDB(OrderBase):
    id: int
    items: List[OrderItemInDB]
