# Librería de formularios
from wtforms import Form, StringField, PasswordField, validators
from wtforms import BooleanField, HiddenField, TextAreaField
from wtforms.fields.html5 import EmailField
from .models import User


def not_admin(form, field):
    if field.data == "admin" or field.data == "root":
        raise validators.ValidationError("Invalid Username.")


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError("You aren't human")


# Esta clase nos permite crear el formulario de Login
class LoginForm(Form):
    username = StringField('Usuario', [
        validators.Length(
            min=4, max=50,
            message='Debe tener un tamaño entre 4 y 50 caracteres')
    ])
    password = PasswordField('Contraseña', [
        validators.Required(message='Por favor, ingrese su contraseña.')
    ])


class RegisterForm(Form):
    honeypot = HiddenField('', [length_honeypot])
    username = StringField('Usuario', [
        validators.Length(min=4, max=50), not_admin
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

    def validate_username(self, username):
        if User.get_by_nickname(username.data):
            raise validators.ValidationError(
                "Este nombre de usuario se encuentra en uso")

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError(
                "Este Correo ya se encuentra en uso")

    def validate(self):
        if not Form.validate(self):
            return False
        if len(self.password.data) < 8:
            self.password.errors.append(
                "La contraseña debe contener mínimo 8 caracteres.")
            return False

        return True


class TaskForm(Form):
    title = StringField('Título', [
                        validators.Length(min=5, max=50,
                                          message="Longitud fuera de rango"),
                        validators.DataRequired(
                            message="El título es obligatorio")
                        ])
    description = TextAreaField('Description', [
        validators.DataRequired(message="Descripción Requerida.")
    ], render_kw={'rows': 8})
