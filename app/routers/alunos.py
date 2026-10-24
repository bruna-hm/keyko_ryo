from fastapi import APIRouter, HTTPException
from app.schemas import AlunoCreate, Aluno, AlunoUpdate
from app.dados import alunos as alunos_dados

router = APIRouter(prefix="/alunos", tags=["alunos"])

def tupla_aluno(aluno): return Aluno(id=aluno[0], nome=aluno[1], contato=aluno[2], ativo=aluno[3])

@router.get("/", response_model=list[Aluno])
def listar_alunos():
    return [tupla_aluno(aluno) for aluno in alunos_dados.listar_alunos()]

@router.get("/{aluno_id}", response_model=Aluno)
def obter_aluno(aluno_id: int):
    aluno = alunos_dados.buscar_aluno(aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return tupla_aluno(aluno)

@router.post("/", response_model=Aluno, status_code=201)
def cadastrar_aluno(aluno: AlunoCreate):
    aluno_id = alunos_dados.cadastrar_aluno(aluno.nome, aluno.contato)
    return tupla_aluno((aluno_id, aluno.nome, aluno.contato, True))

@router.patch("/{aluno_id}", response_model=Aluno)
def editar_aluno(aluno_id: int, dados: AlunoUpdate):
    aluno = alunos_dados.buscar_aluno(aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    enviados = dados.model_dump(exclude_unset=True)
    if "nome" in enviados and enviados["nome"] is None:
        raise HTTPException(status_code=422, detail="O campo 'nome' não pode ser nulo")
    if "nome" in enviados:
        alunos_dados.editar_nome(aluno_id, enviados["nome"])
    if "contato" in enviados:
        alunos_dados.editar_contato(aluno_id, enviados["contato"])
    if "ativo" in enviados:
        alunos_dados.editar_ativo(aluno_id, enviados["ativo"])
    aluno_editado = alunos_dados.buscar_aluno(aluno_id)
    return tupla_aluno((aluno_editado[0], aluno_editado[1], aluno_editado[2], aluno_editado[3]))

@router.delete("/{aluno_id}", status_code=204)
def excluir_aluno(aluno_id: int):
    aluno = alunos_dados.buscar_aluno(aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    alunos_dados.excluir_aluno(aluno_id)
    return None