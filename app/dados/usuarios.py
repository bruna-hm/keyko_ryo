import sqlite3
from app.db import connect_db

def cadastrar_usuario(email, senha_hash):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuarios (email, senha_hash) VALUES (?, ?)", (email, senha_hash))
        con.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        raise ValueError("E-mail inválido ou já cadastrado.")
    finally:
        con.close()
        
def buscar_usuario_por_email(email):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, email, senha_hash FROM usuarios WHERE email = ?", (email,))
        return cursor.fetchone()
    finally:
        con.close()
        
def buscar_usuario_por_id(usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, email, senha_hash FROM usuarios WHERE id = ?", (usuario_id,))
        return cursor.fetchone()
    finally:
        con.close()