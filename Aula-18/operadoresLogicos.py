import sqlite3

conexao = sqlite3.connect("banco_ficticio.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM clientes WHERE cidade = 'Goiânia' AND nome LIKE 'J%'")
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)