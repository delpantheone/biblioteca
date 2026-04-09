from pydantic import BaseModel

class LivroCreate(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: int
    
class LivroOut(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: int