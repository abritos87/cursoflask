from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'Aelton'
    idade = 39

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)

@app.route('/nova/')
def novapag():
    return 'Outra view'