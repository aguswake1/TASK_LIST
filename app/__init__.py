# Pattern design: Singleton
from flask import Flask
from .views import page  # importamos las rutas
from flask_bootstrap import Bootstrap  # importamos bootstrap
# CSRF (Cross-site request forgery) Protection
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from .models import User


app = Flask(__name__)
csrf = CSRFProtect()
db = SQLAlchemy()


def create_app(config):
    # El servidor se configura a traves de un objeto
    app.config.from_object(config)
    Bootstrap().init_app(app)
    # Para validar autenticidad de peticiones mediante tokens
    csrf.init_app(app)
    app.register_blueprint(page)  # indicamos al server que ejecute las rutas

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
