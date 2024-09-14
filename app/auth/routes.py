from flask import Flask,url_for,render_template, request, redirect, flash
from . import auth_bp
from .forms import SignupForm, LoginForm
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
        return redirect(url_for("auth.login"))
    return render_template("auth/signup_form.html", form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        user=form.email.data
        password=form.password.data
        print(f"{user} y {password}")
        return redirect(url_for('public.index'))   
    return render_template('auth/login_form.html', form=form)