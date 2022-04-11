from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from hangout import schemas, database, models
from sqlalchemy.orm import Session
from hangout.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/create',  response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):    
    return user.create(request, db)


