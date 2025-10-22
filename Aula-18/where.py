import sqlite3

conexao = sqlite3.connect("banco_ficticio.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM clientes WHERE cidade = 'Goiânia'")
resultado = cursor.fetchall()

print("\nClientes que moram em goiania:")
for linha in resultado:
    print(linha)

cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'F%'")
resultado = cursor.fetchall()

print("\nClientes com a letra F:")
for linha in resultado:
    print(linha)