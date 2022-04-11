from sqlalchemy.orm import Session
from hangout import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    hangouts = db.query(models.Hangout).all()
    return hangouts


def create(request: schemas.Hangout, db: Session):
    new_hangout = models.Hangout(
    title=request.title,
    content=request.content, 
    date=request.date, 
    )

    db.add(new_hangout)
    db.commit()
    db.refresh(new_hangout)
    return new_hangout


def delete_all(db: Session):
    db.query(models.Hangout).delete()
    db.commit()
    return "ok"