from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import Usuario, UsuarioCreate, UsuarioToken
from app.dados import usuarios as usuarios_dados
from app.seguranca import gerar_hash, gerar_token, verificar_senha
from app.dependencias import usuario_atual

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

@router.post("/login", response_model=UsuarioToken)
def login_usuario(form: OAuth2PasswordRequestForm = Depends()):
    email_limpo = form.username.strip().lower()
    usuario_encontrado = usuarios_dados.buscar_usuario_por_email(email_limpo)
    if usuario_encontrado is None or not verificar_senha(form.password, usuario_encontrado[2]):
        raise HTTPException(
            status_code=401, 
            detail="E-mail ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
            )
    token = gerar_token({"sub": str(usuario_encontrado[0])})
    return UsuarioToken(access_token=token)

@router.get("/me", response_model=Usuario)
def atual(usuario: Optional[tuple] = Depends(usuario_atual)):
    return Usuario(id=usuario[0], email=usuario[1])