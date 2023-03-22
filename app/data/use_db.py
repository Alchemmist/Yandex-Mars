from data.db_session import global_init, create_session
from data import users, jobs
from datetime import date
from data.users import User
from data.jobs import Jobs


# Добавляем капитана
def add_colonials(path_to_db: str) -> None:
    '''Добавляет капитана и 3-х членов экипажа в таблицу users

    Parameters
    ----------
    path_to_db: str
        Путь до файла с sqlite базой данных

    Returns
    -------
    None
    '''

    global_init(path_to_db)
    db_sess = create_session()

    # capitan
    capitan = users.User(name = 'Ridley',
                         surname = 'Scott',
                         age = 21,
                         position = 'capitan',
                         speciality = 'research engineer',
                         address = 'module_1',
                         email = 'scotr_chief@mars.org',
                         modified_date = date.today())
    db_sess.add(capitan)

    # crew
    user1 = users.User(name = 'Bob',
                       surname = 'Marlie',
                       age = 34,
                       position = 'janitor',
                       speciality = 'mop master',
                       address = 'module_1',
                       email = 'mop-bob@gmail.bom',
                       modified_date = date.today())
    user2 = users.User(name = 'Jake',
                       surname = 'Piterson',
                       age = 17,
                       position = 'spiritual leader',
                       speciality = 'philosopher',
                       address = 'module_2',
                       email = 'dzen@gmail.com',
                       modified_date = date.today())
    user3 = users.User(name = 'Anton',
                       surname = 'Grishin',
                       age = 16,
                       position = 'developer',
                       speciality = 'Python programmer',
                       address = 'module_2',
                       email = 'code@gmail.com',
                       modified_date = date.today())


    objects = [
            user1,
            user2,
            user3,
            ]

    db_sess.bulk_save_objects(objects)
    db_sess.commit()


# Первая работа
def add_jobs(path_to_db: str) -> None:
    '''Добавляет задание на развертывание жилых 
    модулей 1 и 2 для экипажа в таблицу jobs 

    Parameters
    ----------
    path_to_db: str
        Путь до файла с sqlite базой данных

    Returns
    -------
    None
    '''

    global_init(path_to_db)
    db_sess = create_session()

    job = jobs.Jobs(team_leader = 1,
                   job = 'deployment of residential modules 1 and 2',
                   work_size = 15,
                   collaborators = '2, 3',
                   start_date = date.today(),
                   is_finished = False)
    db_sess.add(job)
    db_sess.commit()


# Запрос 1
def get_colonials(path_to_db: str) -> None:
    '''Выводит всех колонистов проживающих в 1 модуле

    Parameters
    ----------
    path_to_db: str
        Путь до файла с sqlite базой данных

    Returns
    -------
    None
    '''

    global_init(path_to_db)
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == 'module_1'):
        print(user)


# Запрос 2
def get_no_engineer_colonials(db_name: str) -> None:
    '''Выводит id колонистов проживающих в 1 модуле,
    ни профессия (speciality), ни должность (position) 
    которых не содержат подстроку engineer

    Parameters
    ----------
    path_to_db: str
        Путь до файла с sqlite базой данных

    Returns
    -------
    None
    '''

    global_init(db_name)
    db_sess = create_session()
    for user in db_sess.query(User).filter(
        User.address == "module_1",
        User.speciality.notilike('%engineer%'),
        User.position.notilike('%engineer%')
    ):
        print(user.id)


# Запрос 3
def get_child(path_to_db: str) -> None:
    '''Выводит всех несовершеннолетних (возраст меньше 18) 
    колонистов с указанием возраста в годах

    Parameters
    ----------
    path_to_db: str
        Путь до файла с sqlite базой данных

    Returns
    -------
    None
    '''

    global_init(path_to_db)
    db_sess = create_session()
    for user in db_sess.query(User).filter(
        User.age < 18,
    ):
        print(user, user.age, 'years')

