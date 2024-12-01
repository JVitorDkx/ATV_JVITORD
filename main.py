# Código da aula 01
from flask import Flask

app_JVitor = Flask (__name__)

@app_JVitor.route('/')

def raiz():
    return 'Olá, turma!'
# fea código aula 02
def saudacoes(nome):
    return f'Olá, {nome}'
if __name__ == "_main_":
  app_JVitor.run()