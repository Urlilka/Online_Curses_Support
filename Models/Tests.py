from Models.Base import Base
from peewee import PrimaryKeyField, CharField

class Tests(Base):
    id = PrimaryKeyField()
    test_link = CharField(max_length=255)