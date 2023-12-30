from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import auth
import models
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_merk(db: Session, merk_id: int):
    return db.query(models.Merk).filter(models.Merk.id == merk_id).first()

def get_merk_by_name(db: Session, merk_name: str):
    return db.query(models.Merk).filter(models.Merk.name == merk_name).first()

def get_merken(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Merk).offset(skip).limit(limit).all()

def create_merk(db: Session, merk: schemas.MerkCreate):
    db_merk = models.Merk(name=merk.name)
    db.add(db_merk)
    db.commit()
    db.refresh(db_merk)
    return db_merk

def get_keyboard(db: Session, keyboard_id: int):
    return db.query(models.Keyboard).filter(models.Keyboard.id == keyboard_id).first()

def get_keyboards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Keyboard).offset(skip).limit(limit).all()
    

def create_keyboard(db: Session, keyboard: schemas.KeyboardCreate, merk_id: int):
    db_keyboard = models.Keyboard(**keyboard.dict(), merk_owner_id=merk_id)
    db.add(db_keyboard)
    db.commit()
    db.refresh(db_keyboard)
    return db_keyboard

def get_switch(db: Session, switch_id: int):
    return db.query(models.Switch).filter(models.Switch.id == switch_id).first()

def get_switches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Switch).offset(skip).limit(limit).all()

def create_switch(db: Session, switch: schemas.SwitchCreate, keyboard_id: int):
    db_switch = models.Switch(**switch.dict(), keyboard_id=keyboard_id)
    db.add(db_switch)
    db.commit()
    db.refresh(db_switch)
    return db_switch

def put_merk(db: Session, merk: schemas.MerkCreate, merk_id: int):
    db_merk = db.query(models.Merk).filter(models.Merk.id == merk_id).first()
    db_merk.name = merk.name
    db.commit()
    db.refresh(db_merk)
    return db_merk

def delete_merk(db: Session, merk_id: int):
    db_merk = db.query(models.Merk).filter(models.Merk.id == merk_id).first()
    db.delete(db_merk)
    db.commit()
    return db_merk

def delete_all_merken(db: Session):
    db_merken = db.query(models.Merk).all()
    db.delete(db_merken)
    db.commit()
    return db_merken

def delete_all_keyboards(db: Session):
    db_keyboards = db.query(models.Keyboard).all()
    db.delete(db_keyboards)
    db.commit()
    return db_keyboards

def delete_all_switches(db: Session):
    db_switches = db.query(models.Switch).all()
    db.delete(db_switches)
    db.commit()
    return db_switches


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
