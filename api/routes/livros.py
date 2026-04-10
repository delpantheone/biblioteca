from schemas.livro import LivroOut, LivroCreate, LivroAlterarPreco
from fastapi import APIRouter, HTTPException, Depends, status
from services.biblioteca_service import BibliotecaService
from api.deps import get_biblioteca_service

router = APIRouter(prefix="/livro", tags=["livro"])

@router.post("/", response_model=LivroOut)
def criar(payload: LivroCreate, service: BibliotecaService = Depends(get_biblioteca_service)):
    return service.criar_livro(**payload.__dict__)

@router.get("/{codigo}", response_model=LivroOut)
def obter(codigo: int, service: BibliotecaService = Depends(get_biblioteca_service)):
    if (livro := service.obter_livro(codigo)) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Livro não encontrado")
    return livro

@router.get("/listagem", response_model=list[LivroOut])
def listar(service: BibliotecaService = Depends(get_biblioteca_service)):
    return service.listar_livros()

@router.put("/{codigo}/preco", response_model=LivroOut)
def alterar_valor(codigo: int, payload: LivroAlterarPreco, service: BibliotecaService = Depends(get_biblioteca_service)):
    if (livro := service.alterar_preco_livro(codigo, payload.preco)) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Livro não encontrado")
    return livro
