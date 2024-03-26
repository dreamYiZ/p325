from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/goods/", response_model=schemas.GoodInDB)
def create_good(good: schemas.GoodCreate, db: Session = Depends(get_db)):
    return crud.create_good(db=db, good=good)

@app.post("/goods/list", response_model=List[schemas.GoodInDB])
def read_goods(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    goods = crud.get_goods(db, skip=skip, limit=limit)
    return goods


@app.post("/orders/", response_model=schemas.OrderInDB)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@app.post("/orders/list", response_model=List[schemas.OrderInDB])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

