from fastapi import APIRouter, HTTPException
from app.schemas import Usuario, UsuarioCreate
from app.dados import usuarios as usuarios_dados
from app.seguranca import gerar_hash

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/cadastrar", response_model=Usuario, status_code=201)
def cadastrar_usuario(usuario: UsuarioCreate):
    senha_hash = gerar_hash(usuario.senha)
    email_limpo = usuario.email.strip().lower()
    try:
        usuario_id = usuarios_dados.cadastrar_usuario(email_limpo, senha_hash)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return Usuario(id=usuario_id, email=email_limpo)