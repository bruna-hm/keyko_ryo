from app.db import connect_db

def cadastrar_aula(data, assunto, status):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO aulas (data, assunto, status) VALUES (?, ?, ?)", (data, assunto, status))
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()

def listar_aulas():
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM aulas")
        return cursor.fetchall()
    finally:
        con.close()

def buscar_aula(data):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM aulas WHERE data = ?", (data,))
        return cursor.fetchone()
    finally:
        con.close()

def excluir_aula(aula_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM aulas WHERE id = ?", (aula_id,))
        con.commit()
    finally:
        con.close()
        
def adicionar_alunos(aula_id, aluno_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        print(cursor.execute("PRAGMA database_list").fetchall())
        print(cursor.execute("SELECT id FROM aulas WHERE id = ?", (aula_id,)).fetchall())
        print(cursor.execute("SELECT id FROM alunos WHERE id = ?", (aluno_id,)).fetchall())
        cursor.execute("INSERT INTO aula_aluno (aula_id, aluno_id) VALUES (?, ?)", (aula_id, aluno_id))
        con.commit()
    finally:
        con.close()
    
def editar_status(aula_id, status):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE aulas SET status = ? WHERE id = ?", (status, aula_id))
        con.commit()
    finally:
        con.close()

def editar_data(aula_id, data):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE aulas SET data = ? WHERE id = ?", (data, aula_id))
        con.commit()
    finally:
        con.close()

def editar_assunto(aula_id, assunto):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE aulas SET assunto = ? WHERE id = ?", (assunto, aula_id))
        con.commit()
    finally:
        con.close()