from pydantic import BaseModel


class LivroBase(BaseModel):
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: int


class LivroCreate(LivroBase):
    pass


class LivroOut(LivroBase):
    pass

class LivroAlterarPreco(BaseModel):
    preco: float
