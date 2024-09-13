from flask import render_template
from . import admin_bp
from models import Users


@admin_bp.route("/users/")
def usuarios():
    our_users = (Users.query.order_by(Users.date_added))
    return render_template("admin/users.html", usuarios=our_users)