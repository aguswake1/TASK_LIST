# Implementing MVC structure. Here we are going to find the different routes.
from flask import Blueprint  # This class allow us to do a modularized app
# for rendering templates, for post method
from flask import render_template, request
from .forms import LoginForm

page = Blueprint('page', __name__)


@page.app_errorhandler(404)
def not_found404(error):  # funcion para redireccionar página de error
    # clearing out the type of error
    return render_template('errors/404.html'), 404


@page.route('/')
def index():
    return render_template('index.html', title='Home')


@page.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and LoginForm(request.form).validate():
        print(LoginForm(request.form).username.data)
        print(LoginForm(request.form).password.data)
        print("nueva sesión creada!")
    return render_template('auth/login.html', title='Iniciar Sesión', form=LoginForm(request.form))
