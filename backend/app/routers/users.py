from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from typing import List
from datetime import datetime
from pydantic import BaseModel
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    delete_account,
    update_password
)
app = APIRouter()

class PasswordUpdate(BaseModel):
    new_password : str

@app.post("/users/", response_model = schemas.UserBase)
def add_user(user : schemas.UserCreate, db : Session = Depends(get_db)):
    new_user = create_user(user=user, db=db)
    return new_user


@app.get("/users/", response_model=List[schemas.UserBase])
def show_users(db : Session = Depends(get_db)):
    return get_all_users(db=db)

@app.get("/users/{user_id}", response_model=schemas.UserBase)
def show_user(user_id : int,db : Session = Depends(get_db)):
    return get_user_by_id(id = user_id,db=db)

@app.put("/users/{email}/password")
def edit_password(email : str, payload : PasswordUpdate,db : Session = Depends(get_db)):
    return update_password(email = email, new_password=payload.new_password, db = db)

@app.delete("/users/{email}")
def remove_user(email : str, db : Session = Depends(get_db)):
    return delete_account(email=email, db = db)