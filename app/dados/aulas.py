import sqlite3

from app.db import connect_db

def cadastrar_aula(data, assunto, status, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO aulas (data, assunto, status, usuario_id) VALUES (?, ?, ?, ?)", (data, assunto, status, usuario_id,))
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()

def listar_aulas(usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, data, assunto, status FROM aulas WHERE usuario_id = ?", (usuario_id,))
        return cursor.fetchall()
    finally:
        con.close()

def buscar_aula(aula_id, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, data, assunto, status FROM aulas WHERE id = ? AND usuario_id = ?", (aula_id, usuario_id,))
        return cursor.fetchone()
    finally:
        con.close()

def excluir_aula(aula_id, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM aulas WHERE id = ? AND usuario_id = ?", (aula_id, usuario_id,))
        con.commit()
    finally:
        con.close()
        
def adicionar_alunos(aula_id, aluno_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO aula_aluno (aula_id, aluno_id) VALUES (?, ?)", (aula_id, aluno_id,))
        con.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Aluno já vinculado a esta aula")
    finally:
        con.close()
    
def editar_status(aula_id, status, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE aulas SET status = ? WHERE id = ? AND usuario_id = ?", (status, aula_id, usuario_id,))
        con.commit()
    finally:
        con.close()

def editar_data(aula_id, data, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE aulas SET data = ? WHERE id = ? AND usuario_id = ?", (data, aula_id, usuario_id,))
        con.commit()
    finally:
        con.close()

def editar_assunto(aula_id, assunto, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE aulas SET assunto = ? WHERE id = ? AND usuario_id = ?", (assunto, aula_id, usuario_id,))
        con.commit()
    finally:
        con.close()