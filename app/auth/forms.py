from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField
from wtforms.validators import InputRequired

class RegisterForm(FlaskForm):
    rut = StringField('RUT', validators=[ InputRequired() ])
    password = PasswordField('Contraseña', validators=[ InputRequired() ])

class LoginForm(FlaskForm):
    rut = StringField('RUT', validators=[ InputRequired() ])
    password = PasswordField('Contraseña', validators=[ InputRequired() ])
    next = HiddenField('next')