from flask import Flask,url_for,render_template, request, redirect
from . import auth_bp
from forms import SignupForm

@auth_bp.route('/signup/', methods=['GET', 'POST'])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get("next", None)
        print(f"Usuario:{name}, email {email} y password: {password}. Valor de next: {next}")
        if next:
            return redirect(next)
        return redirect(url_for("public.index"))
    return render_template("auth/signup_form.html", form=form)    
    