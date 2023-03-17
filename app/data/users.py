import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy import (
            orm, 
            Column, 
            String, 
            Integer, 
            DateTime,
        )


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    about = Column(String, nullable=True)
    email = Column(String, 
                              index=True, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.datetime.now)

    news = orm.relationship("News", back_populates='user')
