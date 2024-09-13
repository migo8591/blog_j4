from flask import Flask
from .public import public_bp
from .auth import auth_bp
from .admin import admin_bp
from extensions import db
from flask_login import LoginManager, current_user
from flask_migrate import Migrate

migrate= Migrate()


def create_app(config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config.from_object(config)  # Aplica la configuración
    app.register_blueprint(auth_bp)
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()
 


    return app