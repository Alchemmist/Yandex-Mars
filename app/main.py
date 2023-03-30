from flask import Flask, render_template, redirect
from data.db_session import global_init, create_session
from data.use_db import add_colonials, add_jobs
from forms.user import LoginForm, RegisterForm
from data.users import User


PATH_TO_DB = "../db/mars_explorer.db"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


# Двойная защита
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        astro = db_sess.query(User).filter(User.id == form.id_astro.data).first()
        cap = db_sess.query(User).filter(User.id == form.id_cap.data).first()

        if (astro and astro.check_password(form.password_astro.data)) and \
        (cap and cap.check_password(form.password_cap.data)):
            return redirect("/index")
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
@app.route('/register')
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
            login=form.login.data,
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


if __name__ == '__main__':
    # Добавить капитана и 3-х членов экипажа
    #add_colonials(PATH_TO_DB)

    # Добавить задание на развертывание жилых модулей
    #add_jobs(PATH_TO_DB)

    global_init(PATH_TO_DB)
    app.run()

