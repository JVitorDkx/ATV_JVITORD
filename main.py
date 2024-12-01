# Código da aula 01 e aula 04
from flask import Flask

app_JVitor = Flask (__name__)

# Feature código aula 02
def saudacoes(nome):
    return f'Olá, {nome}'

# Feature código aula 03
@app_JVitor.route('/rota1')
def rota1():
    return 'Olá Usuário!!'

@app_JVitor.route('/rota2')
def rota2():
    resposta = "<h3> Essa é outra página da rota 2 </h3>"
    return resposta

# Feature código aula 04
@app_JVitor.route("/")
def homepage():
    return("homepage.html")

@app_JVitor.route("/contato")
def contato():
    return("contato.html")

# Feature código aula 05
@app_JVitor.route("/index")
def indice():
    return("index.html")
@app_JVitor.route("/usuario")
def dados_usuario():
    nome_usuario="JVitor"
    dados_usuario = {"profissao":"Aluno", "disciplina":"Desenvolvimento Web III"}
    return("usuario.html", nome = nome_usuario, dados = dados_usuario)
# Feature código aula 02
if __name__ == "_main_":
    app_JVitor.run()