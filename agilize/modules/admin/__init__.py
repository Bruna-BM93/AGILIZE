from flask import Blueprint, render_template
from agilize.utils import load_db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/usuarios')
def usuarios():
    db = load_db()
    usuarios = db.get('usuarios', [])
    return render_template('admin/usuarios.html', usuarios=usuarios)