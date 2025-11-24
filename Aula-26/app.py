from flask import Flask, render_template, request, redirect
import banco

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/cadastrar", methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        try:
            import sqlite3
            conn = sqlite3.connect('banco.db')
            c = conn.cursor()

            c.execute("INSERT INTO usuario (nome, email) VALUES (?, ?)", (nome, email))
        except sqlite3.Error as erro:
            print(f"Erro no sqlite: {erro}")
        finally:
            conn.commit()
            conn.close()
    
    return render_template('cadastro.html')

@app.route('/usuarios')
def listar():
    try:
        import sqlite3
        
        conn = sqlite3.connect('banco.db')
        c = conn.cursor()

        c.execute("SELECT * FROM usuario")
        dados = c.fetchall()
    except sqlite3.Error as erro:
        print(f"Erro no sqlite: {erro}")
    finally:
        conn.close()

    return render_template('usuarios.html', usuarios=dados)

@app.route('/usuarios/<int:id>')
def getUser(id):
    try:
        import sqlite3
        
        conn = sqlite3.connect('banco.db')
        c = conn.cursor()

        c.execute("SELECT * FROM usuario WHERE id=?", (id, ))
        usuario = c.fetchone()
    except sqlite3.Error as erro:
        print(f"Erro no sqlite: {erro}")
    finally:
        conn.close()
    
    return render_template('editar.html', usuario = usuario)

@app.route('/atualizar/<int:id>', methods=['POST'])
def alterar(id):
    try:
        import sqlite3
        
        conn = sqlite3.connect('banco.db')
        c = conn.cursor()

        nome = request.form['nome']
        email = request.form['email']

        c.execute("UPDATE usuario SET nome=?, email=? WHERE id=?", (nome, email, id))

        conn.commit()
    except sqlite3.Error as erro:
        print(f"Erro no sqlite: {erro}")
    finally:
        conn.close()
    
    return redirect('/usuarios')

@app.route('/deletar/<int:id>')
def deletar(id):
    try:
        import sqlite3
        
        conn = sqlite3.connect('banco.db')
        c = conn.cursor()

        c.execute("DELETE FROM usuario WHERE id=?", (id, ))

        conn.commit()
    except sqlite3.Error as erro:
        print(f"Erro no sqlite: {erro}")
    finally:
        conn.close()
    
    return redirect('/usuarios')

if __name__ == '__main__':
    app.run(debug=True)