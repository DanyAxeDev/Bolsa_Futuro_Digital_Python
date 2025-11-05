from flask import Flask, render_template, url_for

# Cria a aplicação Flask
app = Flask(__name__)

# Rota para a página inicial ('/')
@app.route('/')
def index():
    return render_template('index.html', titulo='Página Inicial')

# Rota para a página de produtos ('/produtos')
@app.route('/produtos')
def produtos():
    lista_de_produtos = [
        {'nome': 'Notebook Gamer', 'preco': 'R$ 5.000,00','imagem': 'imagens/notebook_gamer.png'},
        {'nome': 'Mouse sem fio', 'preco': 'R$ 150,00', 'imagem': 'imagens/mouse.png'},
        {'nome': 'Teclado Mecânico', 'preco': 'R$ 350,00', 'imagem': 'imagens/teclado.png'},
        {'nome': 'Monitor 4K', 'preco': 'R$ 2.000,00', 'imagem': 'imagens/monitor.png'}
    ]
    return render_template('produtos.html', titulo='Nossos Produtos', produtos=lista_de_produtos)

# Rota para a página de contato ('/contato')
@app.route('/contato')
def contato():
    return render_template('contato.html', titulo='Contato')

# Executa a aplicação em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)