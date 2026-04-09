from repositories.memory import MemoryDB
from services.biblioteca_service import BibliotecaService

db_instance = MemoryDB()

def get_biblioteca_service():
    return BibliotecaService(db=db_instance)