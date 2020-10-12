# Implementing MVC structure. Here we are going to find the routes
from flask import Blueprint  # esta clase sirve para hacer una app modularizada
from flask import render_template  # para renderizar templates


page = Blueprint('page', __name__)


@page.app_errorhandler(404)
def not_found404(error):  # funcion para redireccionar página de error
    return render_template('errors/404.html'), 404  # aclaramos el error


@page.route('/')
def index():
    return render_template('index.html', title='Home')
