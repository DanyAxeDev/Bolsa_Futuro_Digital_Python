import sqlite3

conexao = sqlite3.connect("usuarios.db")

cursor = conexao.cursor()

def createTable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL)
    ''')

def insertUser(nome, email, senha):
    cursor.execute("INSERT INTO users (nome, email, senha) VALUES(?, ?, ?)", (nome, email, senha))
    conexao.commit()

def listUsers():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"\n*************** USUÁRIOS ****************\nId: {user[0]}\nNome: {user[1]}\nE-mail: {user[2]}\n******************************************")

if __name__ == "__main__":
    try:
        createTable()

        while(True):
            print("\n" + "*"*10 + " Sistema de usuários " + "*"*10)
            print("1 - Cadastrar usuário")
            print("2 - Listar usuários")
            print("3 - Sair")

            opcao = input("Digite a opção que deseja: ")

            match(opcao):
                case '1':
                    nome = input("Digite o nome do usuário: ")
                    email = input("Digite o email do usuário: ")
                    senha = input("Digite a senha: ")
                    insertUser(nome, email, senha)
                case '2':
                    listUsers()
                case '3':
                    print("Saindo do sistema...")
                    break

            
        conexao.close()
        
    except sqlite3.Error as erro:
        print(f"Erro no sqlite: {erro}")
