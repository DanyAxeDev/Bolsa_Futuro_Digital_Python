from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/enviar', methods=['POST'])
def exibirInfo():
    if request.method == 'POST':

        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        print(f"Nome: {nome}")
        print(f"Telefone: {telefone}")
        print(f"Email: {email}")

        return "Dados recebidos e exibidos no terminal!"
    
@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('saudacao.html', nome=nome)