from Connection.Connect import connect
from Models.Base import Base
from peewee import PrimaryKeyField, ForeignKeyField
from Models.Curses import Curses
from Models.Videos import Videos

class Videos_Curses(Base):
    id = PrimaryKeyField()
    video_id = ForeignKeyField(Videos)
    curs_id = ForeignKeyField(Curses)

if __name__ == "__main__":
    connect().create_tables([Videos_Curses])