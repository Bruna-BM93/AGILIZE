from flask import Blueprint, render_template
from agilize.utils import load_db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/usuarios')
def usuarios():
    db = load_db()
    usuarios = db.get('usuarios', [])
    return render_template('admin/usuarios.html', usuarios=usuarios)


@bp.route('/financeiro')
def financeiro():
    return render_template('admin/financeiro.html')


@bp.route('/relatorios')
def relatorios():
    return render_template('admin/relatorios.html')


@bp.route('/estoque')
def estoque():
    return render_template('admin/estoque.html')


@bp.route('/vendas')
def vendas():
    return render_template('admin/vendas.html')


@bp.route('/contas_pagar')
def contas_pagar():
    return render_template('admin/contas_pagar.html')


@bp.route('/contas_receber')
def contas_receber():
    return render_template('admin/contas_receber.html')


@bp.route('/fluxo_caixa')
def fluxo_caixa():
    return render_template('admin/fluxo_caixa.html')


@bp.route('/monitoramento')
def monitoramento():
    return render_template('admin/monitoramento.html')


@bp.route('/configuracoes')
def configuracoes():
    return render_template('admin/configuracoes.html')