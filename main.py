# Importando o Flask e o render_template
from flask import Flask, render_template

app_JVitor = Flask(__name__)

# Feature código aula 02 e aula 06
@app_JVitor.route('/<id>')
def saudacoes(id):
    return render_template('homepage.html', nome=id)  # Renderizando o template corretamente

# Feature código aula 03
@app_JVitor.route('/rota1')
def rota1():
    return 'Olá Usuário!!'

@app_JVitor.route('/rota2')
def rota2():
    resposta = "<h3> Essa é uma página da rota 2 </h3>"
    return resposta

# Feature código aula 04
@app_JVitor.route("/")
def homepage():
    return render_template("homepage.html")  # Usando render_template para exibir a página inicial

@app_JVitor.route("/contato")
def contato():
    return render_template("contato.html")  # Renderizando o template 'contato.html'

# Feature código aula 05
@app_JVitor.route("/index")
def indice():
    return render_template("index.html")  # Renderizando o template 'index.html'

@app_JVitor.route("/usuario")
def dados_usuario():
    nome_usuario = "JVitor"
    dados_usuario = {"profissao": "Aluno", "disciplina": "Desenvolvimento Web III"}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usuario)  # Passando dados para o template

# Feature código aula 06
@app_JVitor.route("/usuario/<nome_usuario>;<nome_profissao>;<nome_disciplina>")
def usuario(nome_usuario, nome_profissao, nome_disciplina):
    dados_usuario = {"profissao": nome_profissao, "disciplina": nome_disciplina}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usuario)  # Passando dados dinâmicos

# Feature código aula 02
if __name__ == "__main__":
    app_JVitor.run(debug=True)  # Ativando o modo debug para facilitar o desenvolvimento