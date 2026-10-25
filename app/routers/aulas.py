from fastapi import APIRouter, HTTPException, Depends
from app.dados import aulas as aulas_dados
from app.dados import alunos as alunos_dados 
from app.schemas import AulaCreate, Aula, AulaUpdate
from app.dependencias import usuario_atual

router = APIRouter(prefix="/aulas", tags=["aulas"])

def tupla_aula(aula):  return Aula(id=aula[0], data=aula[1], assunto=aula[2], status=aula[3])

@router.get("/", response_model=list[Aula])
def listar_aulas(usuario = Depends(usuario_atual)):
    return [tupla_aula(aula) for aula in aulas_dados.listar_aulas(usuario[0])]

@router.get("/{aula_id}", response_model=Aula)
def obter_aula(aula_id: int, usuario = Depends(usuario_atual)):
    aula = aulas_dados.buscar_aula(aula_id, usuario[0])
    if not aula:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    return tupla_aula(aula)

@router.post("/", response_model=Aula, status_code=201)
def cadastrar_aula(aula: AulaCreate, usuario = Depends(usuario_atual)):
    aula_id = aulas_dados.cadastrar_aula(aula.data, aula.assunto, aula.status, usuario[0])
    return tupla_aula((aula_id, aula.data, aula.assunto, aula.status))

@router.patch("/{aula_id}", response_model=Aula)
def editar_aula(aula_id: int, dados: AulaUpdate, usuario = Depends(usuario_atual)):
    usuario_id = usuario[0]
    aula = aulas_dados.buscar_aula(aula_id, usuario_id)
    if not aula:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    enviados = dados.model_dump(exclude_unset=True)
    if "data" in enviados and enviados["data"] is None:
        raise HTTPException(status_code=422, detail="O campo 'data' não pode ser nulo")
    if "status" in enviados and enviados["status"] is None:
        raise HTTPException(status_code=422, detail="O campo 'status' não pode estar nulo")
    if "data" in enviados:
        aulas_dados.editar_data(aula_id, enviados["data"], usuario_id)
    if "assunto" in enviados:
        aulas_dados.editar_assunto(aula_id, enviados["assunto"], usuario_id)
    if "status" in enviados:
        aulas_dados.editar_status(aula_id, enviados["status"], usuario_id)
    aula_editada = aulas_dados.buscar_aula(aula_id, usuario_id)
    return tupla_aula(aula_editada)

@router.delete("/{aula_id}", status_code=204)
def excluir_aula(aula_id: int, usuario = Depends(usuario_atual)):
    aula = aulas_dados.buscar_aula(aula_id, usuario[0])
    if not aula:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    aulas_dados.excluir_aula(aula_id, usuario[0])
    return None

@router.post("/{aula_id}/alunos/{aluno_id}", status_code=201)
def vincular_aluno_aula(aula_id: int, aluno_id : int, usuario = Depends(usuario_atual)):
    usuario_id = usuario[0]
    aula = aulas_dados.buscar_aula(aula_id, usuario_id)
    if aula is None:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    aluno = alunos_dados.buscar_aluno(aluno_id, usuario_id)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    try:
        aulas_dados.adicionar_alunos(aula_id, aluno_id)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))