from flask_wtf import FlaskForm
from wtforms import (
        PasswordField, 
        SubmitField, 
        EmailField, 
        BooleanField,
        StringField,
    )
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astro = StringField("id астронавта")
    password_astro = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField("id капитана")
    password_cap = PasswordField("Пароль капитана", validators=[DataRequired()])

    submit = SubmitField('Доступ')
