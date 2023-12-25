from sqlalchemy.orm import Session

import models
import schemas


def get_program(db: Session, platform_id: int):
    return db.query(models.Platform).filter(models.Platform.id == platform_id).first()


def get_program_by_name(db: Session, name: str):
    return db.query(models.Platform).filter(models.Platform.name == name).first()


def get_platforms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Platform).offset(skip).limit(limit).all()


def create_platform(db: Session, platform: schemas.PlatformCreate):
    db_platform = models.Platform(name=platform.name)
    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return db_platform


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def create_platform_game(db: Session, game: schemas.GameCreate, platform_id: int):
    db_game = models.Game(**game.dict(), platform_owner_id=platform_id)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def delete_game(db: Session, game_id: int):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    db.delete(db_game)
    db.commit()
    return db_game
