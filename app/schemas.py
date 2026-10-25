from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class Aluno(BaseModel):
    id: int
    nome: str
    contato: str | None = None
    ativo: bool
    
class AlunoCreate(BaseModel):
    nome: str
    contato: str | None = None
    
class AlunoUpdate(BaseModel):
    nome: str | None = None
    contato: str | None = None
    ativo: bool | None = None
    
class Aula(BaseModel):
    id: int
    data: str
    assunto: str | None = None
    status: str
    
class AulaCreate(BaseModel):
    data: str
    assunto: str | None = None
    status: Literal["agendada", "remarcada", "cancelada", "realizada"] = "realizada"
    
class AulaUpdate(BaseModel):
    data: str | None = None
    assunto: str | None = None
    status: Literal["agendada", "remarcada", "cancelada", "realizada"] | None = None

class Pagamento(BaseModel):
    id : int
    aluno_id : int
    mes_referencia : str
    valor : int 
    data_pagamento : str | None = None
    status : Literal["pago", "pendente"]

class PagamentoCreate(BaseModel):
    aluno_id : int
    mes_referencia : str = Field(pattern=r"^\d{4}-(0[1-9]|1[0-2])$")
    valor : int = Field(gt=0)
    data_pagamento : str | None = None
    status : Literal["pago", "pendente"]
class PagamentoUpdate(BaseModel):
    valor : int | None = Field(default = None, gt=0) 
    data_pagamento : str | None = None
    status : Literal["pago", "pendente"] | None = None
class Usuario(BaseModel):
    id: int
    email: EmailStr
    
class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str = Field(..., min_length=8, max_length=128)
    
class UsuarioToken(BaseModel):
    access_token: str
    token_type: str = "bearer"