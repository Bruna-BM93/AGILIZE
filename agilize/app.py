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
                return redirect(url_for('dashboard'))
        return render_template('login.html', erro='Credenciais inválidas')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    usuario = session.get('usuario')
    if not usuario:
        return redirect(url_for('login'))
    db = load_db()
    pedidos = [p for p in db['pedidos'] if p['status'] != 'finalizado']
    return render_template('dashboard.html', usuario=usuario, pedidos=pedidos)


if __name__ == '__main__':
    app.run(debug=True)