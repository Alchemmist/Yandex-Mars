from flask import Flask, render_template, redirect, request, abort
from data.db_session import global_init, create_session
from data.use_db import add_colonials, add_jobs
from forms.user import LoginForm, RegisterForm
from forms.job import JobForm
from data.users import User
from data.jobs import Jobs
from datetime import datetime
from flask_login import (
        LoginManager, 
        login_user, 
        login_required, 
        logout_user,
        current_user,
    )


PATH_TO_DB = "../db/mars_explorer.db"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)


# Готовимся к миссии
@app.route('/index/<title>')
@app.route('/<title>')
def index(title):
    content = {
        "title": title
    }
    return render_template('base.html', **content)


# Тренировки в полёте
@app.route('/training/<prof>')
def trainging(prof):
    content = {
        "prof": prof,
    }
    return render_template('training.html', **content)


# Список профессий
@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    content = {
        "list_type": list_type,
        "profs_list": [
                "инженер-исследователь", 
                "пилот", 
                "строитель", 
                "экзобиолог", 
                "врач", 
                "инженер по терраформированию", 
                "климатолог", 
                "специалист по радиационной защите", 
                "астрогеолог", 
                "гляциолог", 
                "инженер жизнеобеспечения", 
                "метеоролог", 
                "оператор марсахода", 
                "киберинженер", 
                "штурман", 
                "пилот дроно", 
                ]
    }
    return render_template('list_profs.html', **content)


# Автоматический ответ
@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    content = {
        "title": "Анкета",
        "name": "Mark",
        "surname": "Watny",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True",
    }
    return render_template('auto_answer.html', **content)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# Обработчик формы авторизации
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Аворийный доступ', form=form)


# По каютам!
@app.route('/distribution')
def distribution():
    content = {
            "crew": [
                "Ридли Скотт", 
                "Эниди Уир", 
                "Марк Уотни", 
                "Венката Капур", 
                "Тедди Сандерс", 
                "Шон Бин",
                ]
    }
    return render_template('distribution.html', **content)


# Цвет каюты
@app.route('/table/<male>/<int:age>')
def table(male, age):
    content = {
            "male": male, 
            "age": age,
            }
    return render_template('table.html', **content)


# Форма регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = create_session()
        if db_sess.query(User).filter(User.email == form.login.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.login.data,
            name=form.name.data,
            surname=form.surename.data, 
            age=form.age.data, 
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# Журнал работ
@app.route('/')
def list_jobs():
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


# Добавление работы (обработчик)
@app.route('/add_jobs', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = create_session()
        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job_title.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data,
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Adding a job', form=form)


@app.route("/edit_jobs/<int:id>", methods=["GET", "POST"])
@login_required
def edit_jobs(id):
    form = JobForm()
    if request.method == "GET":
        db_sess = create_session()
        jobs = (
            db_sess.query(Jobs).filter(Jobs.id == id, Jobs.user == current_user).first()
        )
        if jobs:
            form.team_leader.data = jobs.team_leader
            form.job_title.data = jobs.job
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = create_session()
        jobs = (
            db_sess.query(Jobs).filter(Jobs.id == id, Jobs.user == current_user).first()
        )
        if jobs:
            jobs.team_leader = form.team_leader.data
            jobs.job = form.job_title.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data

            db_sess.commit()
            return redirect("/")
        else:
            abort(404)
    return render_template("add_job.html", title="Edit", form=form)


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      Jobs.user == current_user).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


if __name__ == '__main__':
    # Добавить капитана и 3-х членов экипажа
    #add_colonials(PATH_TO_DB)

    # Добавить задание на развертывание жилых модулей
    #add_jobs(PATH_TO_DB)

    global_init(PATH_TO_DB)
    app.run()
