from fastapi import APIRouter, HTTPException
from app.dados import aulas as aulas_dados
from app.schemas import AulaCreate, Aula, AulaUpdate

router = APIRouter(prefix="/aulas", tags=["aulas"])

tupla_aula = lambda aula: Aula(id=aula[0], data=aula[1], assunto=aula[2], status=aula[3])

@router.get("/", response_model=list[Aula])
def listar_aulas():
    return [Aula(id=aula[0], data=aula[1], assunto=aula[2], status=aula[3]) for aula in aulas_dados.listar_aulas()]