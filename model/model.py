from elixir import metadata, Entity, Field
from elixir import Unicode, UnicodeText, Integer
from elixir import setup_all, session
from sqlalchemy import create_engine, pool
from config import *

metadata.bind = create_engine(
    TEST_MYSQL_STR, pool_recycle=3600, pool_size=50, poolclass=pool.SingletonThreadPool)
metadata.bind.echo = True


class User(Entity):

    """
        Custom made bookmark example
    """
    username = Field(Unicode(255))
    password = Field(Unicode(255))
    gender = Field(Integer)
    email = Field(UnicodeText(255))

    def __repr__(self):
        return "<User - username:{0} gender:{1} email:{2}>".format(self.username, self.gender, self.email)

    @classmethod
    def create_user(cls, username, password, gender, email):
        cls(username=username, password=password, gender=gender, email=email)
        session.commit()

    @classmethod
    def get_all_users(cls):
        users = cls.query.filter_by().all()
        return users

    @classmethod
    def search_user_by_username(cls, key):
        users = cls.query.filter(User.username.like('%{}%'.format(key))).all()
        return users


setup_all()
