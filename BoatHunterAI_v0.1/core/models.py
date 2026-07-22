from dataclasses import dataclass
@dataclass
class Boat:
    name:str
    price:int
    location:str
    engine:str
    length:float
    trailer:bool
    score:int=0
    notes:str=""
