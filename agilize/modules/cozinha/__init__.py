from flask import Blueprint, render_template
from agilize.utils import load_db

bp = Blueprint('cozinha', __name__, url_prefix='/cozinha')

@bp.route('/pendentes')
def pendentes():
    db = load_db()
    pedidos = [p for p in db.get('pedidos', []) if p.get('status') != 'pronto']
    return render_template('cozinha/pendentes.html', pedidos=pedidos)
