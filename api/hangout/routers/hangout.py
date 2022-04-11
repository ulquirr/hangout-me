from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from hangout import schemas, database, models
from sqlalchemy.orm import Session
from hangout.repository import hangout

router = APIRouter(
    prefix="/hangout",
    tags=['Hangouts']
)

get_db = database.get_db


@router.get('/')
def all(db: Session = Depends(get_db)):
    return hangout.get_all(db)


@router.post('/create',  response_model=schemas.ShowHangout)
def create(request: schemas.Hangout, db: Session = Depends(get_db)):    
    return hangout.create(request, db)

@router.post('/delete_all')
def delete_all(db: Session = Depends(get_db)):
    return hangout.delete_all(db)


