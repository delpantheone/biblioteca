from dataclasses import dataclass

@dataclass
class Livro:
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float

    def __post_init__(self):
        if self.preco < 0:
            raise ValueError("O preço não pode ser menor que 0")
        if 0 > self.desconto_percentual > 100:
            raise ValueError("O desconto deve estar entre 0 e 100")
        if self.tipo not in {1,2}:
            raise ValueError("Tipo inválido. Use 1 para gratuito e 2 para pago")

    def preco_final(self) -> float:
        if self.tipo == 1:
            return 0.0
        desconto = self.preco * (self.desconto_percentual / 100)
        return (self.preco - desconto)
        
