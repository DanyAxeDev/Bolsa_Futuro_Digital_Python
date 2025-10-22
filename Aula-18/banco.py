import sqlite3

# ==============================
# CONEXÃO COM O BANCO DE DADOS
# ==============================
def criarConexao():
    conexao = sqlite3.connect("banco_ficticio.db")
    return conexao

# ==============================
# CRIAÇÃO DA TABELA CLIENTES
# ==============================
def criarTabelaCliente():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT,
        telefone TEXT,
        cidade TEXT
    );
    """)

# ==============================
# CRIAÇÃO DA TABELA PEDIDOS
# ==============================
def criarTabelaPedidos():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        data DATE,
        valor_total INTEGER,
        status TEXT,
        FOREIGN KEY (client_id) REFERENCES clientes(id)
    );
    """)

# ==============================
# INSERÇÃO DE DADOS FICTÍCIOS
# ==============================
def inserirDadosCliente():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes;")

    clientes = [
        ("Ana Silva", "ana@email.com", "(62)99999-1111", "Goiânia"),
        ("Carlos Oliveira", "carlos@email.com", "(21)88888-2222", "Rio de Janeiro"),
        ("Mariana Costa", "mariana@email.com", "(31)97777-3333", "Belo Horizonte"),
        ("Pedro Santos", "pedro@email.com", "(41)96666-4444", "Aparecida de Goiânia"),
        ("Fernanda Lima", "fernanda@email.com", "(64)95555-5555", "Rio Verde"),
        ("Paulo Abreu", "pauloabreu@email.com", "(62)98555-2333", "Goiânia"),
        ("João Carlos", "joaocarlos@email.com", "(62)96666-4444", "Goiânia")
    ]

    cursor.executemany("""
    INSERT INTO clientes (nome, email, telefone, cidade)
    VALUES (?, ?, ?, ?);
    """, clientes)

    conexao.commit()

def inserirDadosPedidos():
    conexao = criarConexao()
    cursor = conexao.cursor()

    pedidos = [
        (16, '2023-04-18', 1550, "Pendente"),
        (19, '2025-03-22', 430, "Pendente"),
        (18, '2025-09-05', 15, "Entregue"),
    ]

    cursor.executemany("""
    INSERT INTO pedidos (client_id, data, valor_total, status)
    VALUES (?, ?, ?, ?)
    """, pedidos)

    conexao.commit()


# ==============================
# CONSULTAR E MOSTRAR RESULTADOS
# ==============================
def exibirResultadosCliente():
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes;")
    resultados = cursor.fetchall()

    print("\n Lista de clientes cadastrados:\n")

    # Cabeçalho formatado
    print(f"{'Nº':<3} {'ID':<3} {'Nome':<18} {'Email':<25} {'Telefone':<17} {'Cidade'}")
    print("-" * 80)

    # Mostrar dados com índice
    for i, (id_cliente, nome, email, telefone, cidade) in enumerate(resultados, start=1):
        print(f"{i:<3} {id_cliente:<3} {nome:<18} {email:<25} {telefone:<17} {cidade}")

def exibirNomeEvalorTotal():
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute("""SELECT c.nome, p.valor_total
                   FROM clientes c
                   JOIN pedidos p ON c.id = p.client_id
                   WHERE p.valor_total > 100
                   ORDER BY p.valor_total DESC
                   LIMIT 5""")
    
    print("\nPedidos acima de 100:")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

def exibirNomeEvalorAbaixoDe100():
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute("""SELECT c.nome, p.valor_total
                   FROM clientes c
                   JOIN pedidos p ON c.id = p.client_id
                   WHERE p.valor_total < 100
                   ORDER BY p.valor_total DESC
                   LIMIT 5""")
    
    print("\nPedidos abaixo de 100:")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

def exibirPedidosEntregue():
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute("""SELECT c.nome, p.data
                   FROM clientes c
                   JOIN pedidos p ON c.id = p.client_id
                   WHERE p.status = 'Entregue'
                   ORDER BY c.nome DESC
                   LIMIT 5""")
    
    print("\nPedidos entregues:")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

def exibirPedidosPendentes():
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute("""SELECT c.nome, p.data
                   FROM clientes c
                   JOIN pedidos p ON c.id = p.client_id
                   WHERE p.status = 'Pendente'
                   ORDER BY c.nome DESC
                   LIMIT 5""")
    
    print("\nPedidos pendentes:")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

# ==============================
# ENCERRAR CONEXÃO
# ==============================
    conexao.close()

criarTabelaCliente()
criarTabelaPedidos()
exibirNomeEvalorTotal()
exibirNomeEvalorAbaixoDe100()
exibirPedidosEntregue()
exibirPedidosPendentes()