from flask import Flask, render_template, request
import banco

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)