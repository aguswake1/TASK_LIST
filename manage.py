from app import create_app, db, User, Task
from flask_script import Manager, Shell  # esta clase permite levantar servidor
from config import config


config_class = config['development']
app = create_app(config_class)  # le pasamos la clase Config como parámetro


def make_shell_context():
    return dict(app=app, db=db, User=User, Task=Task)


if __name__ == '__main__':
    manager = Manager(app)

    manager.add_command('shell', Shell(make_context=make_shell_context))
    manager.run()
    # python manage.py runserver
    # python manage.py shell (salimos con quit())
