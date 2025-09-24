import sqlite3

conexao = sqlite3.connect("meu_banco.db") # Para criar um banco de dados em memória, use ":memory:" como nome

cursor = conexao.cursor()

def criarTabela():
    try:
        cursor.execute(''' CREATE TABLE IF NOT EXIST alunos 
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       idade INTEGER)
                       ''')
        print("Tabela criada com sucesso")
    except sqlite3.Error as erro:
        print(f"Erro ao acessar o banco de dados: {erro}")

# Inserindo somente um registro
def inserirDado(nome, idade):
    cursor.execute("INSERT INTO aluno (nome, idade) VALUES(?, ?)", (nome, idade))

    conexao.commit()

# Inserindo vários registros
def inserirDados(listaDeAlunos):
    cursor.executemany("INSERT INTO aluno (nome, idade) VALUES(?, ?)", listaDeAlunos)

    conexao.commit()

def getDados():
    cursor.execute("SELECT * FROM alunos")
    return cursor.fetchall()


