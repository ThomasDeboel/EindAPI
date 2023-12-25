from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Platform(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    games = relationship("Game", back_populates="platform_owner")


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_installed = Column(Boolean, default=False)
    platform_owner_id = Column(Integer, ForeignKey("platforms.id"))

    platform_owner = relationship("Platform", back_populates="games")
