import sqlite3

conn = sqlite3.connect("banco.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS usuario(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT
          );''')

conn.commit()
conn.close()