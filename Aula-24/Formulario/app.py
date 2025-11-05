from flask import Flask, render_template, request
from banco import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome_usuario = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        usuarios = getUsers()

        for usuario in usuarios:
            if(email == usuario[2]):
                print("usuario já cadastrado")
                return render_template('existe.html')
            
        addUser(nome_usuario, email, senha)
        return render_template('resultado.html', nome=nome_usuario)
    
    return render_template('cadastro.html')

@app.route('/usuarios')
def usuarios():
    usuarios = getUsers()
    print(usuarios)
    return render_template('usuarios.html', users=usuarios)

if __name__ == '__main__':
    app.run(debug=True)