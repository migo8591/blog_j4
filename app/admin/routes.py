from flask import render_template, redirect, url_for
from . import admin_bp
from models import Users, Posts
from .forms import PostForm
from extensions import db

@admin_bp.route("/users/")
def usuarios():
    our_users = (Users.query.order_by(Users.date_added))
    return render_template("admin/users.html", usuarios=our_users)

@admin_bp.route("/post/", methods=["GET","POST"], defaults={"post_id":None})
@admin_bp.route("/post/<int:post_id>/", methods = ["GET","POST"])
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(titulo = form.title.data, titulo_slug = form.title_slug.data, contenido = form.content.data, bibliografia = form.bible.data)
        db.session.add(post)
        db.session.commit()
        form.title.data =""
        form.title_slug.data =""
        form.content.data =""
        form.bible.data =""
        return redirect(url_for("public.index"))
    return render_template("admin/post.html", form=form)