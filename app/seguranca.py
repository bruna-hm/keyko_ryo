from datetime import datetime, timedelta, timezone

import os
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"
password_hash = PasswordHash.recommended()

def gerar_hash(password):
    return password_hash.hash(password)

def verificar_senha(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def gerar_token(payload, exp_minutes=30):
    payload_copia = payload.copy()
    payload_copia["exp"] = datetime.now(tz=timezone.utc) + timedelta(minutes=exp_minutes)
    return jwt.encode(payload_copia, SECRET_KEY, algorithm=ALGORITHM)

def ler_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except InvalidTokenError:
        raise ValueError("Token inválido ou expirado.")