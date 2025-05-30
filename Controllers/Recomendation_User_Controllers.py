from Models.Recomendations import *
from Models.Users import *
from Models.Recomendations_Users import *

class Recomendation_User_Controllers():

    # Добавление ассоциации Рекоммендация <---> Пользователь
    @classmethod
    def add_recomendation_to_user(cls, recomendation_id, user_id):
        Recomendations_Users.create(
            recomendation_id = recomendation_id,
            user_id = user_id
        )

    # Удаление ассоциации Рекоммендация <---> Пользователь
    @classmethod
    def delete_recomendation_to_user(cls, id):
        Recomendations_Users.delete().where(Recomendations_Users.id == id).execute()


if __name__ == "__main__":
    Recomendation_User_Controllers.add_recomendation_to_user(1,7)