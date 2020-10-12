from app import create_app
from flask_script import Manager  # esta clase permite levantar servidor
from config import config

config_class = config['development']
app = create_app(config_class)  # le pasamos la clase Config como parámetro


if __name__ == '__main__':
    manager = Manager(app)
    manager.run()
    # python manage.py runserver
