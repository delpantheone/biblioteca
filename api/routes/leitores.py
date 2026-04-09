from fastapi import APIRouter, HTTPException, Depends, status
from services.biblioteca_service import BibliotecaService
from api.deps import get_biblioteca_service
from schemas.leitor import LeitorCreate, LeitorOut

router = APIRouter(prefix="/leitor", tags=["leitor"])

@router.get("/", response_model=LeitorOut)
def obter(id: int, service: BibliotecaService = Depends(get_biblioteca_service)):
    if (leitor := service.obter_leitor(id)) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Leitor não encontrado")
    return LeitorOut(**leitor.__dict__)