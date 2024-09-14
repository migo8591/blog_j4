from extensions import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200),  nullable=False)
    correo= db.Column(db.String(200), nullable=False, unique=True)
    contrasena = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    #Create a String
    def __repr__(self):
        return "<Name: %r>"%self.name
    
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    titulo_slug = db.Column(db.String(50), nullable=False)
    contenido = db.Column(db.String(500), nullable=False)
    bibliografia = db.Column(db.String(200))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    

# De nuevo, Flask-login ha pensado en nosotros ya que pone a nuestra disposición la clase UserMixin con una implementación por defecto para todas estas propiedades y métodos. Tan solo tenemos que heredar de ella en nuestra propia clase User.
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
    

users = []


def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None