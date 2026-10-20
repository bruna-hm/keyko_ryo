from db import connect_db, criar_tabelas
import cli

if __name__ == "__main__":
    con = connect_db()
    try:
        criar_tabelas(con)
    finally:
        con.close()
    cli.menu()