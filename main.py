# Código da aula 01
from flask import Flask

app_JVitor = Flask (__name__)

@app_JVitor.route('/')

def raiz():
    return 'Olá, turma!'
# Fea código aula 03
@app_JVitor.route('/rota1')
def rota1():
    return 'Olá Usuáriooo!!'
@app_JVitor.route('/rota2')
def rota2():
    resposta = "<h3> Essa é uma página da rota 2 </h3>"
    return resposta
# Fea código aula 02
if __name__ == "_main_":
    app_JVitor.run()