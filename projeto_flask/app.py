from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    {"nome": "Coca-cola", "descricao": "veneno", "preço": 8.99, "url": "https://gkpb.com.br/wp-content/uploads/2024/02/coca-cola-k-wave-gkpb-banner.jpg"},
    {"nome": "Doritos", "descricao": "suja a mão", "preço": 15.99, "url": "https://wdsgroup.co.uk/wp-content/uploads/2022/04/08907.jpg" },
    {"nome": "Agua", "descricao": "mata sede", "preço": 1.99, "url": "https://www.fusati.com.br/wp-content/uploads/2021/05/O-Que-e-agua-Mineral.jpeg" },
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return render_template("produto.html", produto=produto)
    
    return "Produto não existe!"


# GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

# POST
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = { "nome": nome, "descricao": descricao,}
    lista_produtos.append(produto)
    
    return redirect(url_for("produtos"))

app.run(port=5000)