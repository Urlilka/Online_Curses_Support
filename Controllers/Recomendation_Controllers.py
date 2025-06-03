from Models.Recomendations import *

class Recomendation_Controllers():

    # Добавление Рекомендации
    @classmethod
    def add_recomendation(cls, rec_text):
        Recomendations.create(rec_text = rec_text)

    # вывод всех Рекомендаций
    @classmethod
    def get_recomendations(cls):
        return Recomendations.select().order_by(Recomendations.id.asc())

    # Изменение Рекомендаций
    @classmethod
    def update_recomendation(cls, id, new_text):
        Recomendations.update(rec_text = new_text).where(Recomendations.id == id).execute()

    # Удаление Рекомендации
    @classmethod
    def delete_recomendation(cls, id):
        Recomendations.delete().where(Recomendations.id == id).execute()


if __name__ == "__main__":
    Recomendation_Controllers.add_recomendation(
        "Не так уж и много текста"
    )