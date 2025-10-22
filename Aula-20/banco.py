import sqlite3

# ==============================
# CONEXÃO COM O BANCO DE DADOS
# ==============================
def criarConexao():
    conexao = sqlite3.connect("cinema.db")
    return conexao

# ==============================
# CRIAÇÃO DA TABELA FILME
# ==============================
def criarTabelaFilme():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Filme(
        id_filme INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        duracao INTEGER,
        genero TEXT
    );
    """)

# ==============================
# CRIAÇÃO DA TABELA SESSAO
# ==============================
def criarTabelaSessao():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sessao(
        id_sessao INTEGER PRIMARY KEY AUTOINCREMENT,
        id_filme INTEGER,
        n_sala INTEGER,
        data_hora_inicio DATE,
        preco REAL,
        FOREIGN KEY (id_filme) REFERENCES filme(id_filme),
        FOREIGN KEY (n_sala) REFERENCES Sala(n_sala)
    );
    """)

# ==============================
# CRIAÇÃO DA TABELA SALA
# ==============================
def criarTabelaSala():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sala(
        n_sala INTEGER PRIMARY KEY,
        capacidade_total INTEGER
    );
    """)

# ==============================
# CRIAÇÃO DA TABELA INGRESSO
# ==============================
def criarTabelaIngresso():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ingresso(
        id_ingresso INTEGER PRIMARY KEY AUTOINCREMENT,
        id_sessao INTEGER,
        id_cliente INTEGER,
        data_compra DATE,
        valor_pago REAL,
        FOREIGN KEY (id_sessao) REFERENCES Sessao(id_sessao),
        FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
    );
    """)

# ==============================
# CRIAÇÃO DA TABELA CLIENTE
# ==============================
def criarTabelaCliente():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cliente(
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT
    );
    """)

# ==============================
# CRIAÇÃO DO BANCO
# ==============================
def criarBanco():
    criarTabelaFilme()
    criarTabelaIngresso()
    criarTabelaCliente()
    criarTabelaSala()
    criarTabelaSessao()

# ==============================
# INSERÇÃO DE DADOS FICTÍCIOS
# ==============================
def inserirDadosFilme():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    --> Inserindo filmes
    INSERT INTO Filme (titulo, duracao, genero) VALUES
        ('Matrix', 136, 'Ficção Científica'),
        ('O Poderoso Chefão', 175, 'Drama'),
        ('Vingadores: Ultimato', 181, 'Ação'),
        ('Interestelar', 169, 'Ficção Científica'),
        ('A Origem', 148, 'Ficção Científica'),
        ('Titanic', 195, 'Romance'),
        ('Coringa', 122, 'Drama'),
        ('Avatar', 162, 'Ficção Científica'),
        ('Homem-Aranha: Sem Volta para Casa', 148, 'Ação');
    """)

    conexao.commit()

def inserirDadosSalas():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    --> Inserindo salas
    INSERT INTO Sala (n_sala, capacidade_total) VALUES
        (1, 100),
        (2, 80),
        (3, 60),
        (4, 70),
        (5, 90);
    """)

    conexao.commit()

def inserirDadosSessoes():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    --> Inserindo sessões
    INSERT INTO Sessao (id_filme, n_sala, data_hora_inicio, preco) VALUES
        (1, 1, '2025-10-14 18:00:00', 25.00),
        (2, 2, '2025-10-14 20:00:00', 20.00),
        (3, 1, '2025-10-15 21:30:00', 30.00),
        (4, 3, '2025-10-15 19:00:00', 28.00),
        (5, 2, '2025-10-15 21:00:00', 35.00),
        (6, 4, '2025-10-16 18:30:00', 30.00),
        (7, 5, '2025-10-16 20:00:00', 32.00),
        (8, 1, '2025-10-17 17:00:00', 27.00);
    """)

    conexao.commit()

def inserirDadosClientes():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    --> Inserindo clientes
    INSERT INTO Cliente (nome, email) VALUES
        ('João Silva', 'joao@example.com'),
        ('Maria Oliveira', 'maria@example.com'),
        ('Carlos Souza', 'carlos@example.com'),
        ('Ana Paula', 'ana@example.com'),
        ('Rafael Lima', 'rafael@example.com'),
        ('Fernanda Costa', 'fernanda@example.com'),
        ('Pedro Martins', 'pedro@example.com'),
        ('Luciana Rocha', 'luciana@example.com');
    """)

    conexao.commit()

def inserirDadosIngressos():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    --> Inserindo ingressos
    INSERT INTO Ingresso (id_sessao, id_cliente, data_compra, valor_pago) VALUES
        (1, 1, '2025-10-13', 25.00),
        (1, 2, '2025-10-13', 25.00),
        (2, 3, '2025-10-13', 20.00),
        (1, 3, '2025-10-13', 25.00),
        (1, 4, '2025-10-13', 25.00),
        (4, 5, '2025-10-14', 28.00),
        (5, 6, '2025-10-14', 35.00),
        (6, 7, '2025-10-14', 30.00),
        (7, 8, '2025-10-14', 32.00),
        (8, 9, '2025-10-15', 27.00);
    """)

    conexao.commit()

def inserirDados():
    inserirDadosClientes()
    inserirDadosFilme()
    inserirDadosSalas()
    inserirDadosSessoes()
    inserirDadosIngressos()

# ==============================
# CONSULTA DE CLIENTE E FILME
# ==============================

def getClienteFilme():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT c.nome, f.titulo
    FROM Cliente c
    JOIN Ingresso i ON c.id_cliente = i.id_cliente
    JOIN Sessao s ON i.id_sessao = s.id_sessao
    JOIN Filme f ON s.id_filme = f.id_filme
    """)
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha)

# ==============================
# CONSULTA QUANTIDADE DE INGRESSO POR CLIENTE
# ==============================

def getQtdIngresso():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT c.nome, COUNT (i.id_ingresso) AS total_ingressos
    FROM Cliente c
    JOIN Ingresso i ON c.id_cliente = i.id_cliente
    GROUP BY c.id_cliente
    ORDER BY total_ingressos DESC;
    """)
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha)

# ==============================
# CONSULTA RECEITA FILME
# ==============================

def getReceitaFilme():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT f.titulo, SUM(s.preco) AS receita
    FROM Filme f
    JOIN Sessao s ON f.id_filme = s.id_filme
    GROUP BY f.id_filme
    """)
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha)

# ==============================
# CONSULTA RECEITA SALA
# ==============================

def getReceitaSala():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT s.n_sala, SUM(se.preco) AS receita
    FROM Sala s
    JOIN Sessao se ON s.n_sala = se.n_sala
    GROUP BY s.n_sala
    """)
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha)

# ==============================
# CONSULTA PESSOAS NA SALA
# ==============================

def getQtdSala():
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT
        s.n_sala,
        COUNT(i.id_ingresso) AS quantidade_pessoas,
        sa.capacidade_total - COUNT(i.id_ingresso) AS lugares_restantes
    FROM Sessao s
    JOIN Sala sa ON s.n_sala = sa.n_sala
    LEFT JOIN Ingresso i ON s.id_sessao = i.id_sessao
    GROUP BY s.n_sala, sa.capacidade_total;
    """)
    resultado = cursor.fetchall()

    for linha in resultado:
        print(linha)

criarBanco()
# Rodar somente uma vez
# inserirDados()

getClienteFilme()
print()
getQtdIngresso()
print()
getReceitaFilme()
print()
getReceitaSala()
print()
getQtdSala()

