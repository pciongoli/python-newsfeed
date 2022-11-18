# import Blueprint to let us consolidate routes onto a single bp
from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

# bp object that the parent app can register later - corresponds to using Router middleware of Express
bp = Blueprint('home', __name__, url_prefix='/')

# @bp.route() decorator
# homepage route
@bp.route('/')
def index():
    # get all posts
    db = get_db()
    posts = (
        db
        .query(Post)
        .order_by(Post.created_at.desc())
        .all()
    )

    return render_template(
        'homepage.html',
        posts=posts
        )

# login route
@bp.route('/login')
def logoin():
    return render_template('lgoin.html')

# single-post route - <id> represents a parameter
@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render single post template
    return render_template(
        'single-post.html',
        post=post
        )




