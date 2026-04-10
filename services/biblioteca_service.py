from domain.livro import Livro
from domain.leitor import Leitor
from dataclasses import dataclass
from repositories.memory import MemoryDB

@dataclass
class BibliotecaService:
    db: MemoryDB

    # Leitores
    def criar_leitor(self, id: int, nome: str, email: str) -> Leitor:
        return self.db.leitor_por_id.setdefault(id, Leitor(id, nome, email))

    def obter_leitor(self, id: int) -> Leitor | None:
        return self.db.leitor_por_id.get(id)
        
    def listar_leitores(self):
        return self.db.leitor_por_id.values()

    # Como o dataclass Leitor possui o atributo (frozen=True)
    # ele não pode ser alterado após sua criação

    # Livros

    def criar_livro(self, codigo: int, titulo: str, preco: float, tipo: int, desconto_percentual: float) -> Livro:
        return self.db.livro_por_codigo.setdefault(codigo, Livro(codigo, titulo, preco, tipo, desconto_percentual))

    def obter_livro(self, codigo: int) -> Livro | None:
        return self.db.livro_por_codigo.get(codigo)

    def listar_livros(self):
        return self.db.livro_por_codigo.values()

    def alterar_preco_livro(self, codigo: int, novo_preco: float) -> None | Livro:
        if (livro := self.db.livro_por_codigo.get(codigo)) is None:
            return None
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo")
        livro.preco = novo_preco
        return livro
