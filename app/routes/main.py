from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Página principal de la aplicación."""
    return render_template('index.html')