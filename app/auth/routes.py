from flask import Flask,url_for,render_template, request, redirect, flash
from . import auth_bp
from forms import SignupForm
from models import Users
from extensions import db

@auth_bp.route('/signup/', methods=['GET', 'POST'])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(correo=form.email.data).first()
        if user is None:
            user= Users(nombre=form.name.data,correo=form.email.data,contrasena=form.password.data)
            db.session.add(user)
            db.session.commit()
        form.name.data=""
        form.email.data=""
        form.password.data=""
        flash("User added successfully")
        return redirect(url_for("public.index"))
    return render_template("auth/signup_form.html", form=form)
    # if form.validate_on_submit():
    #     name = form.name.data
    #     email = form.email.data
    #     password = form.password.data
    #     next = request.args.get("next", None)
    #     print(f"Usuario:{name}, email {email} y password: {password}. Valor de next: {next}")
    #     if next:
    #         return redirect(next)
    #     return redirect(url_for("public.index"))
    # return render_template("auth/signup_form.html", form=form)    
    