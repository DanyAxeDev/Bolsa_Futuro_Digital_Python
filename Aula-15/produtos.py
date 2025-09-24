import sqlite3

conexao = sqlite3.connect("produtos.db")

cursor = conexao.cursor()

def createTable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            preco REAL)
    ''')

def insertProduct(nome, preco):
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES(?, ?)", (nome, preco))
    conexao.commit()

def getProduct():
    cursor.execute("SELECT * FROM produtos")
    return cursor.fetchall()

def listarProdutos():
    produtos = getProduct()
    for produto in produtos:
        print(f"\n*********************\nID: {produto[0]}\nNome: {produto[1]}\nPreço: R${produto[2]}")

def deleteProduct(id):
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conexao.commit()

if __name__ == "__main__":
    try:
        createTable()

        while(True):
            print("\n************** LOJA *****************")
            print("1 - Listar produtos")
            print("2 - Cadastrar produto")
            print("3 - Deletar produto")
            print("4 - Sair")

            opcao = input("Digite o comando que deseja executar: ")

            match(opcao):
                case '1':
                    listarProdutos()
                case '2':
                    nome = input("Diga o nome do produto: ")
                    preco = float(input("Diga o preço do produto: "))
                    insertProduct(nome, preco)
                case '3':
                    listarProdutos()
                    id = int(input("\nDigite o id do produto que deseja apagar: "))
                    deleteProduct(id)
                case '4':
                    print("\nSaindo do sistema...")
                    break
                case _:
                    print("Digite um comando válido")

        conexao.close()

    except sqlite3.Error as erro:
        print(f"Erro no sqlite: {erro}")