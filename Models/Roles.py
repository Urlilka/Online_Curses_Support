from Models.Base import Base
from peewee import PrimaryKeyField, CharField

class Roles(Base):
    id = PrimaryKeyField()
    role = CharField(max_length=8)
