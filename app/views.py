from app import app
from flask import render_template

@app.route('/')
def hello():
    nomes = ['klismenia']
    return render_template('index.html',
    title='E quem achar ruim que morra',
    alunos=nomes)
    

