from pydantic import BaseModel

class SwitchBase(BaseModel):
    name: str
    type: str
    keyboard_id: int

class SwitchCreate(SwitchBase):
    pass

class Switch(SwitchBase):
    id: int
    keyboard_parent: int
    
    class Config:
        orm_mode = True

class KeyboardBase(BaseModel):
    naam: str
    is_wireless: bool
    merk_owner_id: int 

class KeyboardCreate(KeyboardBase):
    pass

class Keyboard(KeyboardBase):
    id: int
    merk_owner: int
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