# Pattern design: Singleton
from flask import Flask
from .views import page  # importamos las rutas
from flask_bootstrap import Bootstrap  # importamos bootstrap

app = Flask(__name__)


def create_app(config):
    # El servidor se configura a traves de un objeto
    app.config.from_object(config)
    Bootstrap().init_app(app)
    app.register_blueprint(page)  # indicamos al server que ejecute las rutas
    return app
