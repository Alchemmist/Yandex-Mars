from data.db_session import global_init
from data.users import User
from data.news import News
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


def add_news(db_sess: Session) -> None:
    user = db_sess.query(User).filter(User.id == 1).first()
    news1 = News(
            title="Личная запись", 
            content="Эта запись личная", 
            is_private=True
            )
    news2 = News(
            title="Вторая новость", 
            content="Уже вторая запись!", 
            user=user, 
            is_private=False
            )
    user.news.append(news1)
    user.news.append(news2)
    db_sess.commit()


if __name__ == '__main__':
    global_init("../db/blogs.db")
    db_sess = db_session.create_session()
    add_news(db_sess)
