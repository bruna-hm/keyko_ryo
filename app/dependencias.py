from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.seguranca import ler_token
from app.dados import usuarios as usuarios_dados

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def usuario_atual(token: str = Depends(oauth2_scheme)):
    erro_401 = HTTPException(
        status_code=401,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        dados = ler_token(token)
        usuario_id = int(str(dados["sub"]))
    except ValueError:
        raise erro_401
    usuario = usuarios_dados.buscar_usuario_por_id(usuario_id)
    if usuario is None:
        raise erro_401
    return usuario