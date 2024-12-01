# Código da aula 01
from flask import Flask
app_JVitor = Flask (__name__)
@app_JVitor.route('/')
def raiz():
    return 'Olá, turma!'
app_JVitor.run()