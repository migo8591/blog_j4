from flask import render_template
from . import public_bp
from models import  Posts

@public_bp.route('/')
def index():
    posts = (Posts.query.order_by(Posts.id))
    quantity = posts.count()
    print(f"Contenido de posts: {posts}")
    print(f"Cantidad de posts: {quantity}")
    return render_template('public/index.html', posts=posts, num_post=quantity)
    # return render_template("index.html", num_posts=len(posts), posts=posts)