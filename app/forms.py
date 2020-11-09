# Librería de formularios
from wtforms import Form, StringField, PasswordField, validators


# Esta clase nos permite crear el formulario de Login
class LoginForm(Form):
    username = StringField('Username', [
        validators.Length(min=4, max=50, message='Debe tener un tamaño entre 4 y 50 caracteres')
    ])
    password = PasswordField('Password', [
        validators.Required()
    ])
