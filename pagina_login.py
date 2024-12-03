from flask import Flask, request, redirect, url_for, flash, render_template

app_JVitor = Flask(__name__)
app_JVitor.secret_key = 'chave_secreta'

@app_JVitor.route('/')
def raiz():
    return render_template('index.html')  # Renderiza o arquivo index.html

@app_JVitor.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form['password']
        if validar_senha(senha):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('sucesso'))
        else:
            flash('A senha não atende aos requisitos!', 'error')
    return render_template('login.html')  # Renderiza o arquivo login.html

@app_JVitor.route('/conta', methods=['GET', 'POST'])
def criar_conta():
    if request.method == 'POST':
        senha = request.form['senha']
        confirmacao = request.form['confirmar_senha']
        if senha != confirmacao:
            flash('As senhas não são iguais!', 'error')
        elif not validar_senha(senha):
            flash('A senha não atende aos requisitos!', 'error')
        else:
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('login'))
    return render_template('conta.html')  # Renderiza o arquivo conta.html

@app_JVitor.route('/Ok')
def sucesso():
    return render_template('Ok.html')  # Renderiza o arquivo Ok.html

def validar_senha(senha):
    import re
    # Requisitos: 6 dígitos, 1 maiúscula, 1 número, 1 caractere especial
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
    return bool(re.match(pattern, senha))

if __name__ == '__main__':
    app_JVitor.run()
