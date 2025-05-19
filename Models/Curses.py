from Models.Base import Base
from peewee import PrimaryKeyField, CharField

class Curses(Base):
    id = PrimaryKeyField()
    curs = CharField(max_length=122)