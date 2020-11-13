from flask_mail import Message
from flask import render_template, current_app
from . import mail


def welcome_mail(user):
    message = Message(
        'Verificación de registro',
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[user.email])

    message.html = render_template('email/welcome.html', user=user)
    mail.send(message)
