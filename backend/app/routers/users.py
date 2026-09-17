import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from typing import List
from datetime import datetime
from services.user_service import create_user, get_user, delete_user, update_password, get_users

app = APIRouter()

@app.post("/users/", response_model = schemas.UserBase)
def add_user(user : schemas.UserCreate, db : Session = Depends(get_db)):
    new_user = create_user(user=user, db=db)
    return new_user


@app.get("/users/", response_model=List[schemas.UserBase])
def show_users(db : Session = Depends(get_db)):
    return get_users(db=db)

@app.get("/users/{user_id}", response_model=schemas.UserBase)
def show_user(user_id : int,db : Session = Depends(get_db)):
    return get_user(id = user_id,db=db)

@app.update("/users/{user_id}")
def edit_password(email : str, db : Session = Depends(get_db)):
    return update_password(email = email, db = db)

@app.delete("/users/{email_id}")
def remove_user(email : str, db : Session = Depends(get_db)):
    return delete_user(email=email, db = db)