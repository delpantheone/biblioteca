from pydantic import BaseModel

class LeitorCreate(BaseModel):
    id: int
    nome: str
    email: str

class LeitorOut(BaseModel):
    id: int
    nome: str
    email: str