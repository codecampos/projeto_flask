from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_cpf')
def gerar_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate()
    return render_template('gerar_cpf.html', cpf=cpf_gerado)

@app.route('/gerar_cnpj')
def gerar_cnpj():
    cnpj = CNPJ()
    cnpj_gerado = cnpj.generate()
    return render_template('gerar_cnpj.html', cnpj=cnpj_gerado)

@app.route('/validar_cpf', methods=['GET', 'POST'])
def validar_cpf():
    if request.method == 'POST':
        cpf_digitado = request.form['cpf']
        cpf = CPF()
        valido = cpf.validate(cpf_digitado)
        return render_template('validar_cpf.html', cpf=cpf_digitado, valido=valido)
    return render_template('validar_cpf.html')

@app.route('/validar_cnpj', methods=['GET', 'POST'])
def validar_cnpj():
    if request.method == 'POST':
        cnpj_digitado = request.form['cnpj']
        cnpj = CNPJ()
        valido = cnpj.validate(cnpj_digitado)
        return render_template('validar_cnpj.html', cnpj=cnpj_digitado, valido=valido)
    return render_template('validar_cnpj.html')

if __name__ == '__main__':
    app.run(debug=True)