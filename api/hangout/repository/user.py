from sqlalchemy.orm import Session
from hangout import models, schemas
from fastapi import HTTPException, status
from hangout.hashing import Hash




def create(request: schemas.User, db: Session):
    new_user = models.User(
    login=request.login,
    password=Hash.bcrypt(request.password) 
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

