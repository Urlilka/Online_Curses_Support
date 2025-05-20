from Models.Tests import *

class Test_Controllers():

    # Добавление Теста
    @classmethod
    def add_test(cls,test_link):
        Tests.create(test_link = test_link)

    # Вывод всех тестов
    @classmethod
    def get_tests(cls):
        return Tests.select().order_by(Tests.id.asc())

    # Изменение Теста
    @classmethod
    def update_test(cls, id, new_link):
        Tests.update(test_link = new_link).where(Tests.id == id).execute()

    # Удаление Видео
    @classmethod
    def delete_test(cls, id):
        Tests.delete().where(Tests.id == id).execute()
