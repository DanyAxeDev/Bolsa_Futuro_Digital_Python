livro = {
    "Titulo": "O Senhor dos Anéis",
    "Autor": "J.R.R. Tolkien",
    "Ano": 1954
}

print(f"Título: {livro['Titulo']}")
print(f"Autor: {livro['Autor']}")
print(f"Ano: {livro['Ano']}")

print("\nDetalhes do livro:")
for key, value in livro.items():
    print(f"{key}: {value}")