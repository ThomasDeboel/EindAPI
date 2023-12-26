from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Merk(Base):
    __tablename__ = "merken"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    accesoires = relationship("Keyboard", back_populates="merk_owner")


class Keyboard(Base):
    __tablename__ = "keyboards"

    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String, index=True)
    is_wireless = Column(Boolean, default=False)
    merk_owner_id = Column(Integer, ForeignKey("merken.id"))

    merk_owner = relationship("Merk", back_populates="accesoires")
    switches_owner = relationship("Switch", back_populates="keyboard_parent")

class Switch(Base):
    __tablename__ = "switches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String, index=True)
    keyboard_id = Column(Integer, ForeignKey("keyboards.id"))

    keyboard_parent = relationship("Keyboard", back_populates="switches_owner")
