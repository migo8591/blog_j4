# Indice

- [Introducción](#introducción)
- [Seccion 1](#secci1n-1)
  - [Subsección 1.1](#subsección-11)
- [3. Implementando el formulario](#3-implementando-el-formulario)
- [4. Login de usuario en Flask](#4-login-de-usuario-en-flask)
- [10. Login Codemy Flasker](#10-login-codemy-flasker)
- [11. Update a record in the database Codemy Flasker](#11-update-a-record-in-the-database-codemy-flasker)
- [12. How to migrate database with flask](#12-how-to-migrate-database-with-flask)


- [Conclusión](#conclusión)
# Seccion 1
# 3. Implementando el formulario
1. Crear una ruta para mostrar el formulario con los methods = ['GET', 'POST]
2. Agregar el atributo action e indicar la URL en donde se enviarán los datos del formulario, si se deja vacío será la misma URL desde la que se descargo el recurso. Y en el atributo method = "POST"
2. Incluir un nombre a cada campo del formulario.
3. A la ruta agregar los nombre del formulario con el objeto request del módulo flask
4. Instalar las extensiones Flask-WTF: pip install Flask-WTF y
pip install email-validator
5. Crear un file para crear una clase y utilizando componentes de la extensión Flask-WTF.
6. A la ruta correspondiente se debe importar e instarciar la clase, luego actualizar la vista correspondiente Flask sabrá como hacerlo por medio de  {{ form.xxx.label }} 
7. Agregar la "Secret_key"
8. Para la captura de los datos se hace uso del método validate_on_submit() y ya no se usara request sin form.name.data 

[Volver al Indice](#indice)

# 4. Login de usuario en Flask
***Introduccion a Flask-login***

1. Instalar Flask-login: pip install flask-login
2. Crear una instancia de la clase: LoginManager (debe estar accesible desde cualquier punto de nuestra aplicacion) para ello se crea un objeto de la clase LoginManager que llamaremos login_manager justo después de instanciar la app:
  * from flask_login import LoginManager
  * login_manager = LoginManager(app)

3. Crear un nuevo fichero llamado models.py en el directorio raiz del proyecto para crear el modelo user y añade la clase siguiente: 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash.<br>
Para guardar las contraseñas se utilizara un hash del password: se hace uso de la librería werkzeug.security.<br>
El método check_password comprueba si el hash del parámetro password coincide con el del usuario.

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):

    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)

4. Añade lo siguiente después de la clase User (para guardar los datos en memoria) :
        users = []


        def get_user(email):
            for user in users:
                if user.email == email:
                    return user
            return None

5. Añadir al final del fichero __init__ el siguiente callback que accede al ID que se encuentra almacenado en la sección mediante el método user_loader del objeto login_manager. Pero antes se debe importar: 

from models import users

        @login_manager.user_loader
        def load_user(user_id):
            for user in users:
                if user.id == int(user_id):
                    return user
            return None

6. Para el login de usuarios se tendrá 3 fases:
* Crear la clase del formulario (7)
* Crear la plantilla HTML (8)
* Implementar la vista que realiza el login (9)

8. Abrir el fichero forms.py y agregar pero primero importar: BooleanField

        class LoginForm(FlaskForm):
            email = StringField('Email', validators=[DataRequired()])
            password = PasswordField('Password', validators=[DataRequired()])
            remember_me = BooleanField('Recuérdame')
            submit = SubmitField('Login')
9. Crear la plantilla HTML (login_form.html) para el login_form.html
          {% extends "base_template.html" %}

          {% block title %}Login{% endblock %}

          {% block content %}
              <div>
                  <form action="" method="post" novalidate>
                      {{ form.hidden_tag() }}
                      <div>
                          {{ form.email.label }}
                          {{ form.email }}<br>
                          {% for error in form.email.errors %}
                          <span style="color: red;">{{ error }}</span>
                          {% endfor %}
                      </div>
                      <div>
                          {{ form.password.label }}
                          {{ form.password }}<br>
                          {% for error in form.password.errors %}
                          <span style="color: red;">{{ error }}</span>
                          {% endfor %}
                      </div>
                      <div>{{ form.remember_me() }} {{ form.remember_me.label }}</div>
                      <div>
                          {{ form.submit() }}
                  </div>
              </form>
          </div>
          <div>¿No tienes cuenta? <a href="{{ url_for('show_signup_form') }}">Regístrate</a></div>
        {% endblock %}

10. Implementar la vista que muestre el funcionario de login y compruebe si las credenciales proporcionadas son válidad o no. Añadir la siguiente funcion al fichero __init__.py. Antes se debe import **current_user (Un objeto de usuario {flask-login} si este está autenticado o un usuario animo)** y **login_user (método de flask que autentica al usuario)** de flask_login. Importar la clase :

from werkzeug.urls import url_parse

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            user = get_user(form.email.data)
            if user is not None and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('index')
                return redirect(next_page)
        return render_template('login_form.html', form=form)
11. Aplicar cambios en la vista de registro ("/signup")

# 10. Login Codemy Flasker
1. from werkzeug.security import generate_password_hash, check_password_hash
2. class User(db.Model):
    id:....
    :
    Do some password stuff
    password_hash: db.Column(db.String(128))

    @property
    def password(self)
        raise Attribute("password is not a readable attribute)
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
3. En el archivo form.py
* De wtforms se necesitará PasswordField, BooleanField, ValidationError
password_hash = PasswordField("Enter password", validator=[DataRequired(), EqualTo("password_hash2", message="Passwords must be equal")])
* De wtforms.validators se necesitará EqualTo, Length
password_hash2 = PasswordField("Confirm password", validator=[DataRequired()])
4. Para "hashear" el password se hace desde la ruta antes de guardar los datos del formulario en la variable que los guarda en la database.
    hashed_pw = generate_password_hash(form.password_hash.data, "sha256"). Esta variable se utiliza para guardar en la database.
Video 15

[Volver al Indice](#indice)

# 11. Update a record in the database Codemy Flasker
Video 10

[Volver al Indice](#indice)
# 12. How to migrate database with flask
1. Agregar la columna en la clase - modelo. 
2. Actualizar la clase correspondiente de FlaskForm
3. Crear la variable que guardara la informacion que viene del formulario.
4. Crear la variable que guardara la informacion en la database en la ruta correspondiente.
5. Limpiar form.xxx.data = ""
6. Utilizar donde sea necesario.
7. pip install Flask-Migrate
8. En el __init__.py principal: from frask_migrate import Migrate
9. Instanciar debajo de la instancia db: migrate = Migrate(app, db)
    *Nota: 
        migrate = Migrate()
        def create_app(config=None) -> "Debe llevar None"
            :
            migrate.init_app(app, db)
10. En la consola: flask db init
11. Se crea un a carpeta migrations con versions y alembicios
12. flask db: para ayuda
13. flask db migrate -m "comentario: initial migration"
14. flask db upgrade ("El push")


"So usually when it comes to databases in anything flask, django, ruby on rails any sort of web framework dealing with database is alwayas a two-step process you create a migration and then you push the migration so...We are going to use something called flask migrate to take of all this stuff it's an extension that sort of deals with all this for sql alchemy"
- dash

[Volver al Indice](#indice)
# Seccion 6


[Volver al Indice](#indice)
