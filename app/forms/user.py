from flask_wtf import FlaskForm
from wtforms import (
        PasswordField, 
        SubmitField, 
        BooleanField,
        StringField,
        EmailField,
    )
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class WarningForm(FlaskForm):
    id_astro = StringField("id астронавта")
    password_astro = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField("id капитана")
    password_cap = PasswordField("Пароль капитана", validators=[DataRequired()])

    submit = SubmitField('Доступ')


class RegisterForm(FlaskForm):
    login = StringField("Login/email")
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Register password', validators=[DataRequired()])
    surename = StringField("Surename")
    name = StringField("Name")
    age = StringField("Age")
    position = StringField("Position")
    speciality = StringField("Speciality")
    address = StringField("Address")

    submit = SubmitField('Submit')
