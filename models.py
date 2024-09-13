from extensions import db
from datetime import datetime

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