from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from services.user_service import get_user

def create_admin(email : str,admin : schemas.AdminBase, db : Session = Depends(get_db)):
    #check is admin exists
    current_admin = db.query(models.Users).filter(models.Users.email == email).first()
    if not current_admin:
        raise HTTPException(
            status_code=404,
            detail="Admin does not exist"
        )
    if current_admin.role == "Admin":
        raise HTTPException(
            status_code=401,
            detail = "Admin already existing"
        )
    
    current_admin.role = "Admin"
    db.commit()
    db.refresh(current_admin)
    return True

def get_admin(email : str, db : Session = Depends(get_db)):
    admin = db.query(models.Users).filter(models.Users.email == email).first()
    if not admin:
        raise HTTPException(
            status_code=404,
            detail="Admin does not exist"
        )
    if admin.role != "Admin":
        raise HTTPException(
            status_code=401,
            detail="Admin detail is invalid"
        )
    return admin

def get_users(db : Session = Depends(get_db)):
    return db.query(models.users).all()

def delete_user(email : str, db : Session = Depends(get_db)):
    if not get_user(email):
        raise HTTPException(
            status_code=404,
            detail = "The user does not exist"
        )
    user = db.query(models.users).filter(models.users.email == email).first()
    db.delete(user)
    db.refresh()
    return True