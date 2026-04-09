from dataclasses import dataclass
from domain.leitor import Leitor
from domain.livro import Livro

@dataclass
class MemoryDB:
    leitor_por_id: dict[int, Leitor] = field(default_factory=dict)
    livro_por_codigo: dict[int, Livro] = field(default_factory=dict)