# import Blueprint to let us consolidate routes onto a single bp
from flask import Blueprint, render_template

# bp object that the parent app can register later - corresponds to using Router middleware of Express
bp = Blueprint('home', __name__, url_prefix='/')

# @bp.route() decorator
# homepage route
@bp.route('/')
def index():
    return render_template('homepage.html')

# login route
@bp.route('/login')
def logoin():
    return render_template('lgoin.html')

# single-post route - <id> represents a parameter
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')




