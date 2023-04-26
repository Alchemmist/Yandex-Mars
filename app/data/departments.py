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
    title = Column(String)
    chief = Column(Integer, ForeignKey("users.id"))
    members = Column(String)
    email = Column(String)
