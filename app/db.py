import sqlite3

#PRAGMA é um comando SQL, como o interpretador Python não o reconhece, ele precisa ser executado através do método execute() do cursor. O comando PRAGMA foreign_keys = ON; é usado para habilitar a verificação de integridade referencial no SQLite, garantindo que as chaves estrangeiras sejam respeitadas.

def connect_db():
    con = sqlite3.connect('bancodedados.db')
    con.cursor().execute("PRAGMA foreign_keys = ON;")
    return con

#CHECK é usado para impor restrições de integridade em uma coluna, garantindo que os valores inseridos atendam a determinadas condições. Por exemplo, na tabela alunos, a coluna ativo tem um CHECK que permite apenas os valores 0 ou 1. No SQL não temos o tipo booleano. 

#Existem duas formas de escrever o FOREIGN KEY no SQLite. A primeira forma é definir a chave estrangeira diretamente na coluna, como em aluno_id INTEGER REFERENCES alunos(id). A segunda forma é definir a chave estrangeira como uma restrição separada, usando a sintaxe FOREIGN KEY (aluno_id) REFERENCES alunos(id). Ambas as formas são válidas e funcionam da mesma maneira.

#UNIQUE funciona como uma restrição de integridade que garante que os valores em uma coluna ou combinação de colunas sejam únicos em toda a tabela. No caso da tabela pagamentos, a restrição UNIQUE (aluno_id, mes_referencia) garante que não haja dois registros com o mesmo aluno_id e mes_referencia, evitando duplicidade de pagamentos para o mesmo mês.

def criar_tabelas(con):
    tabelas = """CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL COLLATE NOCASE UNIQUE,
                        senha_hash TEXT NOT NULL
                        );
                    CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
                        nome TEXT NOT NULL,
                        contato TEXT NOT NULL,
                        ativo INTEGER DEFAULT 1 CHECK(ativo IN (0, 1))
                    );
                    CREATE TABLE IF NOT EXISTS aulas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
                        data TEXT NOT NULL,
                        assunto TEXT, 
                        status TEXT CHECK(status IN ('agendada', 'realizada', 'cancelada', 'remarcada')) NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS aula_aluno (
                        aula_id INTEGER NOT NULL REFERENCES aulas(id) ON DELETE CASCADE,
                        aluno_id INTEGER NOT NULL REFERENCES alunos(id) ON DELETE CASCADE,
                        PRIMARY KEY (aula_id, aluno_id)
                    );
                    CREATE TABLE IF NOT EXISTS pagamentos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
                        aluno_id INTEGER NOT NULL REFERENCES alunos(id) ON DELETE CASCADE,
                        mes_referencia TEXT NOT NULL,
                        valor INTEGER NOT NULL,
                        data_pagamento TEXT,
                        status TEXT CHECK(status IN ('pago', 'pendente')) NOT NULL,
                        UNIQUE (aluno_id, mes_referencia)
                    );
                    """
        
    con.cursor().executescript(tabelas)