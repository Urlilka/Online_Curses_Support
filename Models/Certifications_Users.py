from Connection.Connect import connect
from Models.Base import Base
from peewee import PrimaryKeyField, ForeignKeyField
from Models.Certificates import Certificates
from Models.Users import Users

class Certificates_Users(Base):
    id = PrimaryKeyField()
    certificate_id = ForeignKeyField(Certificates)
    user_id = ForeignKeyField(Users)

if __name__ == "__main__":
    connect().create_tables([Certificates_Users])