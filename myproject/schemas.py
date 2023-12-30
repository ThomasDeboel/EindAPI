from pydantic import BaseModel

class SwitchBase(BaseModel):
    name: str
    type: str

class SwitchCreate(SwitchBase):
    pass

class Switch(SwitchBase):
    id: int
    keyboard_id: int
    
    class Config:
        orm_mode = True

class KeyboardBase(BaseModel):
    naam: str
    is_wireless: bool

class KeyboardCreate(KeyboardBase):
    pass

class Keyboard(KeyboardBase):
    id: int
    merk_owner_id: int 
    switches_owner: list[Switch]=[]
    
    class Config:
        orm_mode = True
class MerkBase(BaseModel):
    name: str

class MerkCreate(MerkBase):
    pass

class Merk(MerkBase):
    id: int
    accesoires: list[Keyboard]=[]
    
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
