from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html><head>
    <title>Home page for Thomas's END API </title>
    </head>
    <body>
    <h1> Home page of Thomas's END API</h1>
    <ul>
    <li> <a href="/docs">Documentation</a></li>

    </ul>
    </body>
    </html>
    """

@app.get("/merken/", response_model=list[schemas.Merk])
def read_merken(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    merken = crud.get_merken(db, skip=skip, limit=limit)
    return merken

@app.post("/merken/", response_model=schemas.Merk)
def create_merk(merk: schemas.MerkCreate, db: Session = Depends(get_db)):
    db_merk = crud.get_merk_by_name(db, merk_name=merk.name)
    if db_merk:
        raise HTTPException(status_code=400, detail="Merk already registered")
    return crud.create_merk(db=db, merk=merk)

@app.get("/merken/{merk_id}", response_model=schemas.Merk)
def read_merk(merk_id: int, db: Session = Depends(get_db)):
    db_merk = crud.get_merk(db, merk_id=merk_id)
    if db_merk is None:
        raise HTTPException(status_code=404, detail="Merk not found")
    return db_merk

@app.put("/merken/{merk_id}", response_model=schemas.Merk)
def put_merk(merk_id: int, merk: schemas.MerkCreate, db: Session = Depends(get_db)):
    db_merk = crud.get_merk(db, merk_id=merk_id)
    if db_merk is None:
        raise HTTPException(status_code=404, detail="Merk not found")
    return crud.put_merk(db=db, merk=merk, merk_id=merk_id)

@app.delete("/merken/{merk_id}", response_model=schemas.Merk)
def delete_merk(merk_id: int, db: Session = Depends(get_db)):
    db_merk = crud.get_merk(db, merk_id=merk_id)
    if db_merk is None:
        raise HTTPException(status_code=404, detail="Merk not found")
    return crud.delete_merk(db=db, merk_id=merk_id)

@app.delete("/merken/", response_model=schemas.Merk)
def delete_all_merken(db: Session = Depends(get_db)):
    return crud.delete_all_merken(db=db)

@app.get("/keyboards/", response_model=list[schemas.Keyboard])
def read_keyboards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    keyboards = crud.get_keyboards(db, skip=skip, limit=limit)
    return keyboards

@app.post("/keyboards/", response_model=schemas.Keyboard)
def create_keyboard(
    keyboard: schemas.KeyboardCreate, merk_id: int, db: Session = Depends(get_db)
):
    return crud.create_keyboard(db=db, keyboard=keyboard, merk_id=merk_id)

@app.get("/keyboards/{keyboard_id}", response_model=schemas.Keyboard)
def read_keyboard(keyboard_id: int, db: Session = Depends(get_db)):
    db_keyboard = crud.get_keyboard(db, keyboard_id=keyboard_id)
    if db_keyboard is None:
        raise HTTPException(status_code=404, detail="Keyboard not found")
    return db_keyboard

@app.delete("/keyboards/", response_model=schemas.Keyboard)
def delete_all_keyboards(db: Session = Depends(get_db)):
    return crud.delete_all_keyboards(db=db)

@app.get("/switches/", response_model=list[schemas.Switch])
def read_switches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    switches = crud.get_switch(db, skip=skip, limit=limit)
    return switches

@app.post("/switches/", response_model=schemas.Switch)
def create_switch(
    switch: schemas.SwitchCreate, keyboard_id: int, db: Session = Depends(get_db)
):
    return crud.create_switch(db=db, switch=switch, keyboard_id=keyboard_id)

@app.get("/switches/{switch_id}", response_model=schemas.Switch)
def read_switch(switch_id: int, db: Session = Depends(get_db)):
    db_switch = crud.get_switch(db, switch_id=switch_id)
    if db_switch is None:
        raise HTTPException(status_code=404, detail="Switch not found")
    return db_switch


