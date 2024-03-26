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
