from pydantic import BaseModel
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