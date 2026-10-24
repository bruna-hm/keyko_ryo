from app.db import connect_db

def cadastrar_aluno(nome, contato, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO alunos (nome, contato, usuario_id) VALUES (?, ?, ?)", (nome, contato, usuario_id))
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()
        
def listar_alunos(usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, contato, ativo FROM alunos WHERE usuario_id = ?", (usuario_id,))
        return cursor.fetchall()
    finally:
        con.close()
        
def buscar_aluno(aluno_id, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, contato, ativo FROM alunos WHERE id = ? AND usuario_id= ?", (aluno_id,usuario_id,))
        return cursor.fetchone()
    finally:
        con.close()

def excluir_aluno(aluno_id, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM alunos WHERE id = ? AND usuario_id =?", (aluno_id, usuario_id,))
        con.commit()
    finally:
        con.close()
        
def editar_ativo(aluno_id, ativo, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE alunos SET ativo = ? WHERE id = ? AND usuario_id = ?", (ativo, aluno_id, usuario_id,))
        con.commit()
    finally:
        con.close()

def editar_nome(aluno_id, nome, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE alunos SET nome = ? WHERE id = ? AND usuario_id = ?", (nome, aluno_id, usuario_id))
        con.commit()
    finally:
        con.close()

def editar_contato(aluno_id, contato, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE alunos SET contato = ? WHERE id = ? AND usuario_id = ?", (contato, aluno_id, usuario_id))
        con.commit()
    finally:
        con.close()