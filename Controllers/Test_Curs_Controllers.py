from Models.Tests import *
from Models.Curses import *
from Models.Tests_Curses import *

class Test_Curs_Controllers():

    # Создание ассоциации с Тест <---> Курсы
    @classmethod
    def add_test_to_curs(cls, test_id, curs_id):
        Tests_Curses.create(
            test_id = test_id,
            curs_id = curs_id
        )

    # Удаление асоциации с Тест <---> Курсы
    @classmethod
    def delete_test_to_curs(cls, id):
        Tests_Curses.delete().where(Tests_Curses.id == id).execute()

if __name__ == "__main__":
    Test_Curs_Controllers.add_test_to_curs(1,1)