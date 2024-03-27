from pydantic import BaseModel, Json
from typing import List
from datetime import datetime

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


class OrderBase(BaseModel):
    sn: str
    total: int
    goods: Json
    created_at: datetime
    paid_at: datetime
    payment_amount: float

class OrderCreate(OrderBase):
    pass

class OrderInDB(OrderBase):
    id: int