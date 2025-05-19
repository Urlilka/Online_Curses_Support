from Connection.Connect import connect
from Models.Base import Base
from peewee import PrimaryKeyField, ForeignKeyField
from Models.Curses import Curses
from Models.Users import Users

class Curses_Users(Base):
    id = PrimaryKeyField()
    user_id = ForeignKeyField(Users)
    curs_id = ForeignKeyField(Curses)

if __name__ == "__main__":
    connect().create_tables([Curses_Users])