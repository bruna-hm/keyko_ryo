from fastapi import FastAPI
from app.routers import alunos as alunos_router
from app.routers import auth as auth_router
from app.db import connect_db, criar_tabelas

con = connect_db()
try:
    criar_tabelas(con)
finally:
    con.close()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(alunos_router.router)
app.include_router(auth_router.router)