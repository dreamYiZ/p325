from pydantic import BaseModel

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