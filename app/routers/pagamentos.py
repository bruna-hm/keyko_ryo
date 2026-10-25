from fastapi import APIRouter, HTTPException, Depends
from app.dados import pagamentos as pagamentos_dados
from app.schemas import Pagamento, PagamentoCreate, PagamentoUpdate
from app.dados import alunos as alunos_dados
from app.dependencias import usuario_atual

router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])

def tupla_pagamento(pagamento): return Pagamento(id=pagamento[0], aluno_id=pagamento[1], mes_referencia=pagamento[2], valor=pagamento[3], data_pagamento=pagamento[4], status=pagamento[5])

@router.get("/", response_model=list[Pagamento])
def listar_pagamentos(aluno_id: int, usuario = Depends(usuario_atual)):
    return [tupla_pagamento(pagamento) for pagamento in pagamentos_dados.listar_pagamentos(aluno_id, usuario[0])]

@router.get("/{pagamento_id}", response_model=Pagamento)
def obter_pagamento(pagamento_id : int, usuario = Depends(usuario_atual)):
    pagamento = pagamentos_dados.buscar_pagamento(pagamento_id, usuario[0])
    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return tupla_pagamento(pagamento)

@router.post("/", response_model=Pagamento, status_code=201)
def cadastrar_pagamento(pagamento: PagamentoCreate, usuario = Depends(usuario_atual)):
    usuario_id = usuario[0]
    aluno = alunos_dados.buscar_aluno(pagamento.aluno_id, usuario_id)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    try:
        pagamento_id = pagamentos_dados.cadastrar_pagamento(pagamento.aluno_id, pagamento.mes_referencia, pagamento.valor, pagamento.data_pagamento, pagamento.status, usuario_id)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return tupla_pagamento((pagamento_id, pagamento.aluno_id, pagamento.mes_referencia, pagamento.valor, pagamento.data_pagamento, pagamento.status))

@router.patch("/{pagamento_id}", response_model=Pagamento)
def editar_pagamento(pagamento_id: int, dados : PagamentoUpdate, usuario = Depends(usuario_atual)):
    usuario_id = usuario[0]
    pagamento = pagamentos_dados.buscar_pagamento(pagamento_id, usuario_id)
    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    enviados = dados.model_dump(exclude_unset=True)
    if "valor" in enviados and enviados["valor"] is None:
        raise HTTPException(status_code=422, detail="O campo 'valor' não pode ser nulo")
    if "status" in enviados and enviados["status"] is None:
        raise HTTPException(status_code=422, detail="O campo 'status' não pode ser nulo") 
    if "valor" in enviados:
        pagamentos_dados.editar_valor(pagamento_id, enviados["valor"], usuario_id)
    if "data_pagamento" in enviados:
        pagamentos_dados.editar_datapgt(pagamento_id, enviados["data_pagamento"], usuario_id)
    if "status" in enviados:
        pagamentos_dados.editar_statuspgt(pagamento_id, enviados["status"], usuario_id)
    pagamento_editado = pagamentos_dados.buscar_pagamento(pagamento_id, usuario_id)
    return tupla_pagamento(pagamento_editado)

@router.delete("/{pagamento_id}", status_code=204)
def excluir_pagamento(pagamento_id: int, usuario = Depends(usuario_atual)):
    pagamento = pagamentos_dados.buscar_pagamento(pagamento_id, usuario[0])
    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    pagamentos_dados.excluir_pagamento(pagamento_id, usuario[0])
    return None