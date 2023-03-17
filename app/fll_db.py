from data.users import User
from data import db_session
from sqlalchemy.orm import Session


def add_user(db_sess: Session) -> None:
    user = User(
            name = "Пользователь 1",
            about = "биография пользователя 1",
            email = "email@email.ru"
            )
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__mai__':
    db_sess = db_session.create_session()
    add_user(db_sess)
