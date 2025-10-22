import sqlite3

conexao = sqlite3.connect("banco_ficticio.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM clientes")

resultado = cursor.fetchall()

print("Lista de cliente com todos os dados:")
for linha in resultado:
    print(linha)

cursor.execute("SELECT nome, email FROM clientes")

resultado = cursor.fetchall()

print("Lista de cliente com nome e email")
for linha in resultado:
    print(linha)