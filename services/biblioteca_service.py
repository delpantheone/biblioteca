from domain.livro import Livro
from domain.leitor import Leitor
from dataclasses import dataclass
from repositories.memory import MemoryDB

@dataclass
class BibliotecaService:
    db: MemoryDB

    def criar_leitor(self, id: int, nome: str, email: str) -> Leitor:
        leitor = Leitor(id, nome, email)
        self.db.leitor_por_id[id] = leitor
        return self.db.leitor_por_id[id] 

    def obter_leitor(self, id: int) -> Leitor | None:
        leitor = self.db.leitor.get(id)
        return leitor