from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db

# url_prefix='/dashboard' - prefix every route in the blueprint with /dashboard
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# dashboard route
@bp.route('/')
def dash():
    db = get_db()
    posts = (
        db.query(Post)
        .filter(Post.user_id == session.get('user_id'))
        .order_by(Post.created_at.desc())
        .all()
    )

    return render_template(
        'dashboard.html',
        posts=posts,
        loggedIn=session.get('loggedIn')
    )

# edit-post route
@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')

