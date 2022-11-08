from flask import Blueprint, render_template
# url_prefix='/dashboard' - prefix every route in the blueprint with /dashboard
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# dashboard route
@bp.route('/')
def dash():
    return render_template('dashboard.html')

# edit-post route
@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')

