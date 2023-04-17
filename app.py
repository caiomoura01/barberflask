from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return (render_template('index.html'))


@app.route('/login.html')
def login():
    return (render_template('login.html'))

@app.route('/autenticar.html', methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['password']:
        return redirect('/')
    else:
        return redirect('/login.html')


@app.route('/cadastrar.html')
def cadastrar():
    return (render_template('cadastrar.html'))


app.run(debug=True)
