# Pattern design: Singleton
from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap  # importamos bootstrap
# CSRF (Cross-site request forgery) Protection
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
bootstrap = Bootstrap()
login_manager = LoginManager()


from .views import page  # importamos las rutas
from .models import User


def create_app(config):
    # El servidor se configura a traves de un objeto
    app.config.from_object(config)
    # Para validar autenticidad de peticiones mediante tokens
    mail.init_app(app)
    csrf.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = '.login'
    login_manager.login_message = "Inicie sesión para acceder a las Tareas"

    app.register_blueprint(page)  # indicamos al server que ejecute las rutas

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
