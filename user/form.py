__author__ = 'Joshua'

from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):
    # username = StringField('username', [validators.Required()])
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=35)
    ])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=4, max=35)
    ])

    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=35)
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=4, max=35)
    ])


