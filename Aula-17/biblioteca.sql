CREATE TABLE livros (
    ISBN TEXT PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano INTEGER,
    editora TEXT
);

CREATE TABLE autores (
    ID_autor TEXT PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE usuarios (
    ID_usuario TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT,
    telefone TEXT
);

CREATE TABLE autores_livros (
    ISNB_livro TEXT NOT NULL,
    ID_autor TEXT NOT NULL,
    PRIMARY KEY (ISBN_livro, ID_autor),
    FOREIGN KEY (ISBN_livro) REFERENCES livros(ISBN)
    FOREIGN KEY (ID_autor) REFERENCES autores(ID_autor)
);

CREATE TABLE emprestimos (
    ID_emprestimo TEXT PRIMARY KEY,
    ISBN_livro TEXT NOT NULL,
    ID_usuario TEXT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE,
    FOREIGN KEY (ISBN_livro) REFERENCES livros(ISBN)
    FOREIGN KEY (ID_usuario) REFERENCES usuarios(ID_usuario)
);