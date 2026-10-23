from app.db import connect_db

def cadastrar_aluno(nome, contato):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO alunos (nome, contato) VALUES (?, ?)", (nome, contato))
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()
        
def listar_alunos():
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, contato, ativo FROM alunos")
        return cursor.fetchall()
    finally:
        con.close()
        
def buscar_aluno(aluno_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
        return cursor.fetchone()
    finally:
        con.close()

def excluir_aluno(aluno_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
        con.commit()
    finally:
        con.close()
        
def editar_ativo(aluno_id, ativo):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE alunos SET ativo = ? WHERE id = ?", (ativo, aluno_id))
        con.commit()
    finally:
        con.close()

def editar_nome(aluno_id, nome):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE alunos SET nome = ? WHERE id = ?", (nome, aluno_id))
        con.commit()
    finally:
        con.close()

def editar_contato(aluno_id, contato):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE alunos SET contato = ? WHERE id = ?", (contato, aluno_id))
        con.commit()
    finally:
        con.close()