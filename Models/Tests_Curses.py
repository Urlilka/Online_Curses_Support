from Connection.Connect import connect
from Models.Base import Base
from peewee import PrimaryKeyField, ForeignKeyField
from Models.Curses import Curses
from Models.Tests import Tests

class Tests_Curses(Base):
    id = PrimaryKeyField()
    test_id = ForeignKeyField(Tests)
    curs_id = ForeignKeyField(Curses)

if __name__ == "__main__":
    connect().create_tables([Tests_Curses])