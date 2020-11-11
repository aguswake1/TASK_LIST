# Librería de formularios
from wtforms import Form, StringField, PasswordField, validators, BooleanField
from wtforms.fields.html5 import EmailField


# Esta clase nos permite crear el formulario de Login
class LoginForm(Form):
    username = StringField('Usuario', [
        validators.Length(
            min=4, max=50, message='Debe tener un tamaño entre 4 y 50 caracteres')
    ])
    password = PasswordField('Contraseña', [
        validators.Required(message='Por favor, ingrese su contraseña.')
    ])


class RegisterForm(Form):
    username = StringField('Usuario', [
        validators.Length(min=4, max=50)
    ])
    email = EmailField('Correo', [
        validators.Length(min=6, max=100),
        validators.Required(message='Debe ingresar su email!'),
        validators.Email(message='Ingrese un correo válido')
    ])
    password = PasswordField('Contraseña', [
        validators.Required(message='Ingrese la contraseña'),
        validators.EqualTo('confirm_password',
                           message='Las contraseñas no coinciden')
    ])
    confirm_password = PasswordField('Confirmar contraseña', [
        validators.Required(message='Confirme la contraseña')
    ])
    accept = BooleanField('', [
        validators.DataRequired()
    ])
