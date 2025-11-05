import sqlite3

def get_connection():
    # Cria uma nova conexão em cada chamada
    return sqlite3.connect("usuariosFormulario.db", check_same_thread=False)
    
cursor = get_connection().cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        senha TEXT);
''')

def addUser(nome, email, senha):
    try:
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conexao.commit()
        print("Usuario cadastrado com sucesso")
    except sqlite3.Error as erro:
        print(f"Erro no sqlite: {erro}")
    finally:
        conexao.close()

def getUsers():
    try:
        cursor = get_connection().cursor()
        cursor.execute("SELECT * FROM users")
        
        resultado = cursor.fetchall()

        return resultado
    except sqlite3.Error as erro:
        print(f"Erro no sqlite: {erro}")