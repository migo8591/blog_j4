from flask import Flask,url_for,render_template, request, redirect, flash
from . import auth_bp
from .forms import SignupForm, LoginForm
from models import Users, User, users, get_user
from extensions import db
# from werkzeug.urls import url_parse
from urllib.parse import urlparse
from flask_login import current_user, login_user

@auth_bp.route('/signup/', methods=['GET', 'POST'])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        # user=Users.query.filter_by(correo=form.email.data).first()
        # if user is None:
        #     user= Users(nombre=form.name.data,correo=form.email.data,contrasena=form.password.data)
        #     db.session.add(user)
        #     db.session.commit()
        # form.name.data=""
        # form.email.data=""
        # form.password.data=""
        # flash("User added successfully")
        name = form.name.data
        email = form.email.data
        password = form.password.data
        #  ↓ Creamos el usuario y lo guardamos: 
        user = User(len(users)+1, name, email, password)
        users.append(user)
        print(users)
        print(type(users))
        print(f"Nombre del usuario: {user.name}")
        print(f"Nombre del email: {user.email}")
        print(f"Nombre del password: {user.password}")
        print(len(users))
        
        #Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        # if not next_page or url_parse (next_page).netloc != '':
        #     next_page = url_parse('public.index')
        if not next_page or urlparse (next_page).netloc != '':
            next_page = urlparse('public.index')
        return redirect(url_for("auth.login"))
    return render_template("auth/signup_form.html", form=form)



@auth_bp.route('/login', methods=['GET', 'POST'])
def login(): 
    # Se comprueba si el usuario ya está autenticado:
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        # Si existe un con dicho email y la contraseña coincide se procede a autenticar al usuario llamando al método login_user
        if user is not None and user.check_password(form.password.data):
            #  ↑ Si las credenciales son correctas, se inicia sesión para el usuario. El parámetro remember=form.remember_me.data indica si el usuario quiere que se recuerde su sesión (por ejemplo, mediante una cookie persistente).
            login_user(user, remember=form.remember_me.data)
            #Por último comprobaremos si recibimos el parametro next. Esto sucedera cuando el usuario ha intentado acceder a una pagina protegida pero no esta autenticado. Por temas de seguridad solo tendremos en cuenta dicho parámetro si la ruta es relativa. 
            next_page = request.args.get('next')
            # ↑ El parámetro next indica a qué página debe redirigir el sistema una vez que el usuario haya iniciado sesión. Si un usuario intentaba acceder a una página que requiere autenticación (como /dashboard), se le redirigiría primero a la página de inicio de sesión con un parámetro next que contiene la URL de destino: http://localhost:5000/login?next=/dashboard
            # ↓ Si no se recibe el parámetro next o este no contiene una relativa redirigimos al usuario a la pagina de inicio 
            if not next_page or urlparse(next_page).netloc !='':
                # ↑ Si next_page tiene un netloc no vacio lo considera insegura y lo redireccionar a la pagina principal
                next_page = url_for('public.index')
            return redirect(next_page)
    return render_template('auth/login_form.html', form=form)

#Acerca de las rutas relativas:
# Una ruta relativa es aquella que no incluye el dominio completo. En este caso, la ruta '/login' es una ruta relativa porque solo define la dirección después de la raíz del servidor. Por ejemplo, si la aplicación se ejecuta en http://localhost:5000, entonces la URL completa sería http://localhost:5000/login.

# Ejemplo con parámetro next
# Imagina que el usuario intenta acceder a /dashboard, pero no está autenticado. Flask lo redirigiría a la página de inicio de sesión con el parámetro next que indica a dónde debe ser redirigido después de iniciar sesión.

# Por ejemplo, la URL a la que se le redirige sería:
# http://localhost:5000/login?next=/dashboard
# Si el usuario inicia sesión correctamente, será redirigido a /dashboard en lugar de ser enviado a la página principal.


# Explicación de "url_parse(next_page).netloc !='' "


    # if not next_page or url_parse(next_page).netloc != '':

# tiene una función importante para asegurar que el parámetro next_page sea una URL interna (dentro del mismo sitio web) y no una URL externa (de otro dominio). Vamos a desglosarlo:

# Explicación de url_parse(next_page).netloc != '':
# url_parse(next_page):

# La función url_parse proviene de werkzeug.urls y sirve para descomponer una URL en sus componentes: esquema (http o https), dominio (netloc), ruta, parámetros, etc. Es similar a lo que hace la función urlparse en la biblioteca estándar de Python.
# Por ejemplo, si next_page es "http://example.com/dashboard", url_parse(next_page) devuelve un objeto que contiene:

# scheme: "http"
# netloc: "example.com" (dominio)
# path: "/dashboard"
# url_parse(next_page).netloc:

# El atributo netloc representa el dominio (y opcionalmente el puerto) de una URL. Si next_page es una URL externa (como "http://example.com/dashboard"), netloc será "example.com".

# Si next_page es una URL relativa dentro de tu aplicación (por ejemplo, "/dashboard"), el netloc será una cadena vacía ('') porque no tiene dominio.

# url_parse(next_page).netloc != '':

# Esta condición se asegura de que el valor de netloc no esté vacío, lo que significa que next_page contiene un dominio externo. Si netloc != '', la URL sería externa, lo cual podría representar un problema de seguridad (por ejemplo, un ataque de redireccionamiento malicioso).
# Contexto de seguridad:
# El propósito de este código es evitar redirecciones no seguras a dominios externos. Si next_page fuera una URL externa, el usuario podría ser redirigido a otro sitio web fuera de tu control, lo que abre la posibilidad a ataques como phishing o redireccionamientos maliciosos.

# Por eso, si next_page tiene un netloc no vacío, el código lo considera inseguro y establece un valor por defecto:

# python
# Copy code
# next_page = url_for('index')
# Esto garantiza que, si alguien intentara redirigir al usuario a un sitio externo, tu aplicación lo devolvería de manera segura a la página de inicio.

# Ejemplo práctico:
# Si next_page es "/dashboard", el valor de netloc será '' porque no hay dominio. En este caso, la redirección es segura y el usuario será enviado a "/dashboard".

# Si next_page es "http://example.com/dashboard", el valor de netloc será "example.com", lo que indica una URL externa. En este caso, la redirección se considerará insegura y el usuario será redirigido a la página de inicio (/index).

# Esta condición es un control de seguridad crucial en aplicaciones web que manejan redirecciones basadas en parámetros.

# https://chatgpt.com/share/66e5d4ea-02d0-800d-a6d5-42a1e0949e22




