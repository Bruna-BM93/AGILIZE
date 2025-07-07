from flask import Blueprint, render_template
from agilize.utils import load_db

bp = Blueprint('garcom', __name__, url_prefix='/garcom')

@bp.route('/mesas')
def mesas():
    db = load_db()
    pedidos = db.get('pedidos', [])
    return render_template('garcom/mesas.html', pedidos=pedidos)