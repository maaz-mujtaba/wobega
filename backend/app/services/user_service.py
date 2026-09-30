from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import models
from app import schemas
from app.database import get_db
import uuid
from typing import List
from datetime import datetime
import app.security as security
import app.schemas as schemas

def get_user_by_email(email : str, db : Session ):
    user = db.query(models.Users).filter(models.Users.email == email).first()
    return user

def get_user_by_id(id : int, db : Session):
    user = db.query(models.Users).filter(models.Users.user_id == id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User does not exist"
        )
    return user

def  get_all_users(db : Session):
    return db.query(models.Users).all()

def create_user(user : schemas.UserCreate, db : Session):
    if (get_user_by_email(email = user.email, db = db)):
        raise HTTPException(
            status_code=401,
            detail = "User already exists"
        )
    
    secure_password = security.hash_password(user.hash_password)
    new_user = models.Users(
        #user_id = uuid.uuid4().int & (1 << 63)-1,
        name = user.name,
        email = user.email,
        hash_password = secure_password,
        role = user.role,
        phone = user.phone
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_password(email : str, new_password : str ,db : Session):
    #check if user exists
    existing_user = get_user_by_email(email = email, db = db)

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User does not exist"
        )
    
    #check if new_password == old password
    flag = security.verify_password(new_password,existing_user.hash_password)
    if flag:
        return{
            "message" : "Password is same as the stored password"
        }
    
    existing_user.hash_password = security.hash_password(new_password)
    db.commit()
    db.refresh(existing_user)
    return {"message" : "Password updated successfully"}


def delete_account(email : str, db : Session):
    user = get_user_by_email(email=email, db = db)
    if not user:
        raise HTTPException(
            status_code=404,
            detail = "The user does not exist"
        )
    db.delete(user)
    db.refresh()
    return True