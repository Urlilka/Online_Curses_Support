from Models.Base import Base
from peewee import PrimaryKeyField, CharField

class Certificates(Base):
    id = PrimaryKeyField()
    cert_link = CharField(max_length=255)
