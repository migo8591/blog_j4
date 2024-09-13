from flask import render_template, redirect, url_for
from . import admin_bp
from models import Users
from .forms import PostForm


@admin_bp.route("/users/")
def usuarios():
    our_users = (Users.query.order_by(Users.date_added))
    return render_template("admin/users.html", usuarios=our_users)

@admin_bp.route("/post/", methods=["GET","POST"], defaults={"post_id":None})
@admin_bp.route("/post/<int:post_id>/", methods = ["GET","POST"])
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data
        
        post = {"title": title, "title_slug": title_slug, "content": content}
        return redirect(url_for("public.index"))
    return render_template("admin/post_form.html", form=form)