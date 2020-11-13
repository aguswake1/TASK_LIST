# Implementing MVC structure. Here we are going to find the different routes.
from flask import Blueprint  # This class allow us to do a modularized app
# for rendering templates, for post method
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Task
from .forms import LoginForm, RegisterForm, TaskForm
from . import login_manager
from .email import welcome_mail

page = Blueprint('page', __name__)


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)


@page.app_errorhandler(404)
def not_found404(error):  # funcion para redireccionar página de error
    # clearing out the type of error
    return render_template('errors/404.html'), 404


@page.route('/')
def index():
    return render_template('index.html', title='Home')


@page.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('.task'))

    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.create_element(
                form.username.data, form.password.data, form.email.data)
            flash('Registro exitoso!', 'success')
            login_user(user)
            welcome_mail(user)
            return redirect(url_for('.task'))

    return render_template('auth/register.html', title='Registro', form=form,
                           active='register')


@page.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.task'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.get_by_nickname(form.username.data)
        if user and user.verify_password(form.password.data):
            # la función recibe un objeto de tipo UserMixin
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('.task'))
        else:
            flash('Usuario o contraseña incorrectos.', 'error')
    return render_template('auth/login.html', title='Iniciar Sesión',
                           form=form, active='login')


@page.route('/logout')
def logout():
    # Función de la libreria flask_login
    logout_user()
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('.login'))


@page.route('/tasks')
@page.route('/tasks/<int:page>')
@login_required
def task(page=1, per_page=6):
    # obtenemos todas las tareas del usuario (relación uno a muchos)
    pagination = current_user.tasks.paginate(page, per_page=per_page)
    tasks = pagination.items

    return render_template('task/list.html', title='Tareas', tasks=tasks,
                           pagination=pagination, page=page, active='task')


@page.route('/tasks/show/<int:task_id>')
def seeing_task(task_id):
    task = Task.query.get_or_404(task_id)

    return render_template('task/show.html', title='Tarea', task=task)


@page.route('/tasks/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm(request.form)

    if request.method == 'POST' and form.validate():
        task = Task.create_element(
            form.title.data, form.description.data, current_user.id)
        if task:
            flash("Tarea creada con éxito", 'success')
            return redirect(url_for('.task'))
    return render_template('task/new.html', title='Nueva Tarea', form=form,
                           active='new_task')


@page.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def editar(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        abort(404)

    form = TaskForm(request.form, obj=task)

    if request.method == 'POST' and form.validate():
        task = Task.save_edit(task.id, form.title.data, form.description.data)

        if task:
            flash("Tarea Actualizada", 'success')
            return redirect(url_for('.task'))

    return render_template('task/edit.html', title='Editar Tarea', form=form)


@page.route('/tasks/delete/<int:task_id>', methods=['GET', 'POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        abort(404)

    if Task.delete_element(task.id):
        flash("Tarea Eliminada")

    return redirect(url_for('.task'))
