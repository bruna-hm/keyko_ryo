import traceback

print("1. iniciando")
try:
    from app.db import connect_db
    print("2. import ok")
    conn = connect_db()
    print("3. conectou")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS aula_aluno")
    print("4. aula_aluno apagada")
    cur.execute("DROP TABLE IF EXISTS pagamentos")
    print("5. pagamentos apagada")
    conn.commit()
    conn.close()
    print("Tabelas apagadas.")
except Exception:
    traceback.print_exc()

input("Enter para sair")