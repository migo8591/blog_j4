from flask import render_template
from . import admin_bp


@admin_bp.route("/users/")
def usuarios():
    return render_template("admin/users.html")