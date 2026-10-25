import sqlite3
from app.db import connect_db

def cadastrar_pagamento(aluno_id, mes_referencia, valor, data_pagamento, status, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO pagamentos (aluno_id, mes_referencia, valor, data_pagamento, status, usuario_id) VALUES (?, ?, ?, ?, ?, ?)", (aluno_id, mes_referencia, valor, data_pagamento, status, usuario_id,))
        con.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        raise ValueError("Pagamento deste aluno já cadastrado neste mês")
    finally:
        con.close()

def listar_pagamentos(aluno_id, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, aluno_id, mes_referencia, valor, data_pagamento, status FROM pagamentos WHERE aluno_id = ? AND usuario_id = ?", (aluno_id, usuario_id,))
        return cursor.fetchall()
    finally:
        con.close()

def buscar_pagamento(pagamento_id, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT id, aluno_id, mes_referencia, valor, data_pagamento, status FROM pagamentos WHERE id = ? AND usuario_id = ?", (pagamento_id, usuario_id,))
        return cursor.fetchone()
    finally:
        con.close()

def excluir_pagamento(pagamento_id, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM pagamentos WHERE id = ? AND usuario_id = ?", (pagamento_id, usuario_id,))
        con.commit()
    finally:
        con.close()
        
def editar_statuspgt(pagamento_id, status, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE pagamentos SET status = ? WHERE id = ? AND usuario_id = ?", (status, pagamento_id, usuario_id,))
        con.commit()
    finally:
        con.close()
        
def editar_datapgt(pagamento_id, data_pagamento, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE pagamentos SET data_pagamento = ? WHERE id = ? AND usuario_id = ?",(data_pagamento, pagamento_id, usuario_id,))
        con.commit()
    finally:
        con.close()

def editar_valor(pagamento_id, valor, usuario_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE pagamentos SET valor = ? WHERE id = ? AND usuario_id = ?", (valor, pagamento_id, usuario_id,))
        con.commit()
    finally:
        con.close()