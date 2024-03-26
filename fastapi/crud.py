from sqlalchemy.orm import Session

import models
import schemas



def create_good(db: Session, good: schemas.GoodCreate):
    db_good = models.Good(**good.dict())
    db.add(db_good)
    db.commit()
    db.refresh(db_good)
    return db_good

def get_goods(db: Session, skip: int = 0, limit: int = 100):
    goods = db.query(models.Good).offset(skip).limit(limit).all()
    return goods



def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict(exclude={"items"}))
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        db_item = models.OrderItem(**item.dict(), order_id=db_order.id)
        db.add(db_item)
    db.commit()

    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    orders = db.query(models.Order).offset(skip).limit(limit).all()
    return orders


