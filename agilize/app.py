from flask import Flask, render_template, request, redirect, url_for, session
from .utils import load_db

from .modules.caixa import bp as caixa_bp
from .modules.cozinha import bp as cozinha_bp
from .modules.garcom import bp as garcom_bp
from .modules.admin import bp as admin_bp

app = Flask(__name__)
app.secret_key = 'CHANGE_ME'

app.register_blueprint(caixa_bp)
app.register_blueprint(cozinha_bp)
app.register_blueprint(garcom_bp)
app.register_blueprint(admin_bp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        db = load_db()
        for u in db['usuarios']:
            if u['usuario'] == usuario and u['senha'] == senha:
                session['usuario'] = usuario
                session['funcao'] = u.get('funcao', 'adm')
                return redirect(url_for('dashboard'))
        return render_template('login.html', erro='Credenciais inválidas')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    usuario = session.get('usuario')
    funcao = session.get('funcao')
    if not usuario:
        return redirect(url_for('login'))
    db = load_db()
    pedidos = [p for p in db['pedidos'] if p['status'] != 'finalizado']
    if funcao == 'garcom':
        return redirect(url_for('garcom.mesas'))
    if funcao == 'caixa':
        return redirect(url_for('caixa.pedidos'))
    if funcao == 'cozinha':
        return redirect(url_for('cozinha.pendentes'))
    return render_template('dashboard.html', usuario=usuario, pedidos=pedidos, funcao=funcao)


if __name__ == '__main__':
    app.run(debug=True)