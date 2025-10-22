import sqlite3

conexao = sqlite3.connect("banco_ficticio.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM clientes ORDER BY nome ASC")
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)