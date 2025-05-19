from Models.Base import Base
from peewee import PrimaryKeyField, CharField

class Videos(Base):
    id = PrimaryKeyField()
    video_link = CharField(max_length=255)