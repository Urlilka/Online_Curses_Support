from Models.Base import Base
from peewee import PrimaryKeyField, TextField

class Recomendations(Base):
    id = PrimaryKeyField()
    rec_text = TextField()
