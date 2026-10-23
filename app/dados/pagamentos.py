from app.db import connect_db

def cadastrar_pagamento(aluno_id, mes_referencia, valor, data_pagamento, status):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO pagamentos (aluno_id, mes_referencia, valor, data_pagamento, status) VALUES (?, ?, ?, ?, ?)", (aluno_id, mes_referencia, valor, data_pagamento, status))
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()

def listar_pagamentos():
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM pagamentos")
        return cursor.fetchall()
    finally:
        con.close()

def editar_pagamento(pagamento_id, aluno_id, mes_referencia, valor, data_pagamento, status):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE pagamentos SET aluno_id = ?, mes_referencia = ?, valor = ?, data_pagamento = ?, status = ? WHERE id = ?", (aluno_id, mes_referencia, valor, data_pagamento, status, pagamento_id))
        con.commit()
    finally:
        con.close()

def excluir_pagamento(pagamento_id):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM pagamentos WHERE id = ?", (pagamento_id,))
        con.commit()
    finally:
        con.close()
        
def editar_statuspgt(pagamento_id, status):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE pagamentos SET status = ? WHERE id = ?", (status, pagamento_id))
        con.commit()
    finally:
        con.close()
        
def editar_datapgt(pagamento_id, data_pagamento):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE pagamentos SET data_pagamento = ? WHERE id = ?", (data_pagamento, pagamento_id))
        con.commit()
    finally:
        con.close()

def editar_valor(pagamento_id, valor):
    con = connect_db()
    try:
        cursor = con.cursor()
        cursor.execute("UPDATE pagamentos SET valor = ? WHERE id = ?", (valor, pagamento_id))
        con.commit()
    finally:
        con.close()