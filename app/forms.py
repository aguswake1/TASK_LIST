# Librería de formularios
from wtforms import Form, StringField, PasswordField, validators


# Esta clase nos permite crear el formulario de Login
class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50)
    ])
    password = PasswordField('Password', [
        validators.Required()
    ])
