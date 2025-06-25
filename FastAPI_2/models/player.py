from pydantic import BaseModel

class Player(BaseModel):
    numero: int = 0
    nombre: str = ""
    edad: int = 0
    posicion: str = ""
    imagen: str = ""