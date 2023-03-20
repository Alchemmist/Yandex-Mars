import json
from flask import Flask,  render_template, redirect, request, abort
from data import db_session
from data.news import News
from data.users import User
from forms.user import RegisterForm, LoginForm
from forms.news import NewsForm
from flask_login import (
        LoginManager, 
        login_user, 
        login_required, 
        logout_user,
        current_user,
    )


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/index/<title>')
@app.route('/<title>')
def index(title):
    content = {
        "title": title
    }
    return render_template('base-готовимся_к_миссии.html', **content)


@app.route('/training/<prof>')
def train(prof):
    content = {
        "prof": prof,
    }
    return render_template('training.html', **content)


if __name__ == '__main__':
    db_session.global_init("../db/blogs.db")
    app.run()
