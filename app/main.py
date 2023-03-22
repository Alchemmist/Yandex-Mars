from flask import (
        Flask, 
        render_template, 
        )
from data.db_session import global_init, create_session
from data.use_db import (
        add_colonials, 
        add_jobs,
        )


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


if __name__ == '__main__':
    # Добавить капитана и 3-х членов экипажа
    #add_colonials(PATH_TO_DB)

    # Добавить задание на развертывание жилых модулей
    #add_jobs(PATH_TO_DB)

    global_init(PATH_TO_DB)
    app.run()

