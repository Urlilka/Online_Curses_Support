from Connection.Connect import connect
from Models.Base import Base
from peewee import PrimaryKeyField, ForeignKeyField
from Models.Recomendations import Recomendations
from Models.Users import Users

class Recomendations_Users(Base):
    id = PrimaryKeyField()
    recomendation_id = ForeignKeyField(Recomendations)
    user_id = ForeignKeyField(Users)

if __name__ == "__main__":
    connect().create_tables([Recomendations_Users])