from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import (
            Column, 
            ForeignKey,
            String, 
            Integer,
            DateTime, 
            Boolean,
        )


# Модель Работы
class Jobs(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey('users.id'))
    job = Column(String, nullable=True)
    work_size = Column(Integer, nullable=True)
    collaborators = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    is_finished = Column(Boolean, nullable=True)

    user = orm.relationship("User")

