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
    <title>Home page for Thomas's API </title>
    </head>
    <body>
    <h1> Home page of Thomas's API</h1>
    <ul>
    <li> <a href="/docs">Documentation</a></li>
    <li> <a href="/platforms/">Platforms</a></li>
    <li> <a href="/games/">Games</a></li>
    </ul>
    </body>
    </html>
    """
@app.post("/platforms/", response_model=schemas.Platform)
def create_platform(platforms: schemas.PlatformCreate, db: Session = Depends(get_db)):
    db_platform = crud.get_program_by_name(db, name=platforms.name)
    if db_platform:
        raise HTTPException(status_code=400, detail="Platform name already exist")
    return crud.create_platform(db=db, platform=platforms)


@app.get("/platforms/", response_model=list[schemas.Platform])
def read_platforms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    platforms = crud.get_platforms(db, skip=skip, limit=limit)
    return platforms


@app.get("/platforms/{platform_id}", response_model=schemas.Platform)
def read_platforms(platform_id: int, db: Session = Depends(get_db)):
    db_platform = crud.get_program(db, platform_id=platform_id)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform


@app.post("/platforms/{platform_id}/games/", response_model=schemas.Game)
def create_game_for_platform(
    platform_id: int, game_id: schemas.GameCreate, db: Session = Depends(get_db)
):
    return crud.create_platform_game(db=db, game=game_id, platform_id=platform_id)


@app.get("/games/", response_model=list[schemas.Game])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games

@app.delete("/platforms/{platform_id}/games/{game_id}", response_model=schemas.Game)
def delete_game(platform_id: int, game_id: int, db: Session = Depends(get_db)):
    db_game = crud.delete_game(db=db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game

