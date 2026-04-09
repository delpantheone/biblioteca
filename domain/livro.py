@dataclass
class Livro:
    codigo: int
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: int

    def preco_final(self) -> float:
        if self.tipo == 1:
            self.preco = 0
            return self.preco
        if self.preco < 0:
            raise ValueError("O preço não pode ser menor que 0")
        if self.tipo == 2 and self.desconto_percentual in range(0,100):
            desconto = (self.preco * self.desconto_percentual) / 100
            return (self.preco - desconto)
        