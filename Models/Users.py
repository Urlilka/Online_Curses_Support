from flask_login import UserMixin
from Connection.Connect import connect
from Models.Base import Base
from peewee import PrimaryKeyField, ForeignKeyField, CharField
from Models.Roles import Roles
from Models.Recomendations import Recomendations
from Models.Certificates import Certificates
from Models.Curses import Curses
from Models.Tests import Tests
from Models.Videos import Videos



class Users(UserMixin,Base):
    id = PrimaryKeyField()
    username = CharField(max_length=15)
    password = CharField(max_length=30)
    firstname = CharField(max_length=25)
    surname = CharField(max_length=25)
    role_id = ForeignKeyField(Roles)

if __name__ == "__main__":
    connect().create_tables([
        Tests,
        Curses,
        Roles,
        Videos,
        Certificates,
        Recomendations,
        Users,
    ])