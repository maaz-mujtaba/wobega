import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from typing import List

app = APIRouter()

@app.get("/users/", response_model=List[schemas.UserBase])
def get_users(db : Session = Depends(get_db)):
    return db.query(models.users).all()

@app.get("/users/{user_id}", response_model=schemas.UserBase)
def get_user(user_id : int,db : Session = Depends(get_db)):
    user = db.query(models.users).filter(models.users.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User does not exist")
    return user

@app.post("/users/", response_model = schemas.UserBase)
def create_user(user : schemas.UserCreate, db : Session = Depends(get_db)):
    
    #Check is user already exists
    existing_user = db.query(models.users).filter(models.user.email_id == user.email_id).first()
    if existing_user:
        raise HTTPException(status_code = 401, detail="User Already exits")
    
    new_user = models.users(
        user_id = uuid.uuid4(),
        name = user.name,
        email_id = user.email_id,
        hashed_password = f"hashed_{user.password}",
        is_active = True,
        role = user.role,
        created_at = user.created_at,
        updated_at = user.created_at
    ) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.update("/users/{user_id}")
def update_password(id : int, db : Session = Depends(get_db)):
    pass

@app.delete("/users/{user_id}")
def delete_user(id : int, db : Session = Depends(get_db)):

    #Check if user does not exist
    user = db.query(models.users).filter(models.users.user_id == id).first()
    if not user:
        raise HTTPException(
            status_code = 404,
            detail = "User does not exist"
        )
    
    db.delete(user)
    db.refresh()