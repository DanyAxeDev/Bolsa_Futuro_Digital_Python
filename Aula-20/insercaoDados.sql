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

--> Inserindo salas
INSERT INTO Sala (n_sala, capacidade_total) VALUES
(1, 100),
(2, 80),
(3, 60),
(4, 70),
(5, 90);

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

--> Inserindo ingressos
INSERT INTO Ingresso (id_sessao, id_cliente, data_compra, valor_pago) VALUES
(1, 1, '2025-10-13', 25.00),
(1, 2, '2025-10-13', 25.00),
(2, 3, '2025-10-13', 20.00);

-- Sessão 1
INSERT INTO Ingresso (id_sessao, id_cliente, data_compra, valor_pago) VALUES
(1, 3, '2025-10-13', 25.00),
(1, 4, '2025-10-13', 25.00);

-- Sessão 4 (Titanic)
INSERT INTO Ingresso (id_sessao, id_cliente, data_compra, valor_pago) VALUES
(4, 5, '2025-10-14', 28.00);

-- Sessão 5 (Coringa)
INSERT INTO Ingresso (id_sessao, id_cliente, data_compra, valor_pago) VALUES
(5, 6, '2025-10-14', 35.00);

-- Sessão 6 (Avatar)
INSERT INTO Ingresso (id_sessao, id_cliente, data_compra, valor_pago) VALUES
(6, 7, '2025-10-14', 30.00);

-- Sessão 7 (Homem-Aranha)
INSERT INTO Ingresso (id_sessao, id_cliente, data_compra, valor_pago) VALUES
(7, 8, '2025-10-14', 32.00);

-- Sessão 8 (Matrix)
INSERT INTO Ingresso (id_sessao, id_cliente, data_compra, valor_pago) VALUES
(8, 9, '2025-10-15', 27.00);