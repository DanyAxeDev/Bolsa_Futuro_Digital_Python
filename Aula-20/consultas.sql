SELECT c.nome, f.titulo
FROM Clientes c
JOIN Ingresso i ON c.id_cliente = i.id_cliente
JOIN Sessao s ON i.id_sessao = s.id_sessao
JOIN Filme f ON s.id_filme = f.id_filme

SELECT c.nome, COUNT (i.id_ingresso) AS total_ingressos
FROM Cliente c
JOIN Ingresso i ON c.id_cliente = i.id_cliente
GROUP BY c.id_cliente
ORDER BY total_ingressos DESC;

SELECT f.titulo, SUM(s.preco) AS receita
FROM Filme f
JOIN Sessao s ON f.id_filme = s.id_filme
GROUP BY f.id_filme

SELECT s.n_sala, SUM(se.preco) AS receita
FROM Sala s
JOIN Sessao se ON s.n_sala = se.n_sala
GROUP BY s.n_sala

SELECT
    s.n_sala,
    COUNT(i.id_ingresso) AS quantidade_pessoas,
    sa.capacidade_total - COUNT(i.id_ingresso) AS lugares_restantes
FROM Sessao s
JOIN Sala sa ON s.n_sala = sa.n_sala
LEFT JOIN Ingresso i ON s.id_sessao = i.id_sessao
GROUP BY s.n_sala, sa.capacidade_total;