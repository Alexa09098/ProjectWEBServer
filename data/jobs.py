import datetime
import sqlalchemy
from sqlalchemy import orm

from db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    genre = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    price = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    bought = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Book> {self.book}'
