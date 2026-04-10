from fastapi import APIRouter, Depends, HTTPException, status

from api.deps import get_biblioteca_service
from schemas.leitor import LeitorCreate, LeitorOut
from services.biblioteca_service import BibliotecaService

router = APIRouter(prefix="/leitor", tags=["leitor"])


@router.post("/", response_model=LeitorOut)
def criar(
    payload: LeitorCreate, service: BibliotecaService = Depends(get_biblioteca_service)
):
    return service.criar_leitor(**payload.__dict__)


@router.get("/", response_model=LeitorOut)
def obter(id: int, service: BibliotecaService = Depends(get_biblioteca_service)):
    if (leitor := service.obter_leitor(id)) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Leitor não encontrado")
    return LeitorOut(**leitor.__dict__)


@router.get("/listagem", response_model=list[LeitorOut])
def listar(service: BibliotecaService = Depends(get_biblioteca_service)):
    return service.listar_leitores()
