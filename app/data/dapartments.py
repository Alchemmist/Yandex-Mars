from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase
from sqlalchemy import (
        Column, 
        String, 
        Integer,
        ForeignKey, 
    )


# Еще одна модель
class Department(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    chief = Column(Integer, nullable=True)
    members = Column(Integer, ForeignKey("uers_list.department_id"), nullable=True)
    email = Column(String, nullable=True)


class UsersList(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "users_list"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    department_id = Column(Integer)
