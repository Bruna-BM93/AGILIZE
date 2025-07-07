from flask import Blueprint, render_template
from agilize.utils import load_db

bp = Blueprint('caixa', __name__, url_prefix='/caixa')

@bp.route('/pedidos')
def pedidos():
    db = load_db()
    pedidos = db.get('pedidos', [])
    return render_template('caixa/pedidos.html', pedidos=pedidos)