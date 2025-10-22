CREATE TABLE IF NOT EXISTS Filme(
    id_filme INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    duracao INTEGER,
    genero TEXT
);

CREATE TABLE IF NOT EXISTS Sessao(
    id_sessao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_filme INTEGER,
    n_sala INTEGER,
    data_hora_inicio DATE,
    preco REAL,
    FOREIGN KEY (id_filme) REFERENCES filme(id_filme),
    FOREIGN KEY (n_sala) REFERENCES Sala(n_sala)
);

CREATE TABLE IF NOT EXISTS Sala(
    n_sala INTEGER PRIMARY KEY,
    capacidade_total INTEGER
);

CREATE TABLE IF NOT EXISTS Ingresso(
    id_ingresso INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sessao INTEGER,
    id_cliente INTEGER,
    data_compra DATE,
    valor_pago REAL,
    FOREIGN KEY (id_sessao) REFERENCES Sessao(id_sessao),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE IF NOT EXISTS Cliente(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
);