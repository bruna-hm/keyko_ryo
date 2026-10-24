from fastapi import APIRouter, Depends, HTTPException
from app.schemas import AlunoCreate, Aluno, AlunoUpdate
from app.dados import alunos as alunos_dados
from app.dependencias import usuario_atual

router = APIRouter(prefix="/alunos", tags=["alunos"])

def tupla_aluno(aluno): return Aluno(id=aluno[0], nome=aluno[1], contato=aluno[2], ativo=aluno[3])

@router.get("/", response_model=list[Aluno])
def listar_alunos(usuario = Depends(usuario_atual)):
    return [tupla_aluno(aluno) for aluno in alunos_dados.listar_alunos(usuario[0])]

@router.get("/{aluno_id}", response_model=Aluno)
def obter_aluno(aluno_id: int, usuario = Depends(usuario_atual)):
    aluno = alunos_dados.buscar_aluno(aluno_id, usuario[0])
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return tupla_aluno(aluno)

@router.post("/", response_model=Aluno, status_code=201)
def cadastrar_aluno(aluno: AlunoCreate, usuario = Depends(usuario_atual)):
    aluno_id = alunos_dados.cadastrar_aluno(aluno.nome, aluno.contato, usuario[0])
    return tupla_aluno((aluno_id, aluno.nome, aluno.contato, True))

@router.patch("/{aluno_id}", response_model=Aluno)
def editar_aluno(aluno_id: int, dados: AlunoUpdate, usuario = Depends(usuario_atual)):
    usuario_id = usuario[0]
    aluno = alunos_dados.buscar_aluno(aluno_id, usuario_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    enviados = dados.model_dump(exclude_unset=True)
    if "nome" in enviados and enviados["nome"] is None:
        raise HTTPException(status_code=422, detail="O campo 'nome' não pode ser nulo")
    if "nome" in enviados:
        alunos_dados.editar_nome(aluno_id, enviados["nome"], usuario_id)
    if "contato" in enviados:
        alunos_dados.editar_contato(aluno_id, enviados["contato"], usuario_id)
    if "ativo" in enviados:
        alunos_dados.editar_ativo(aluno_id, enviados["ativo"], usuario_id)
    aluno_editado = alunos_dados.buscar_aluno(aluno_id, usuario_id)
    return tupla_aluno(aluno_editado)

@router.delete("/{aluno_id}", status_code=204)
def excluir_aluno(aluno_id: int, usuario = Depends(usuario_atual)):
    aluno = alunos_dados.buscar_aluno(aluno_id, usuario[0])
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    alunos_dados.excluir_aluno(aluno_id, usuario[0])
    return None