from Models.Curses import *

class Curs_Controllers:

    # Добавление курса
    @classmethod
    def add_curs(cls,curs_name):
        Curses.create(curs = curs_name)

    # Вывод всех курсов
    @classmethod
    def get_curs(cls):
        return Curses.select().order_by(Curses.curs.asc())

    # Вывод одной записи по id
    @classmethod
    def show_curs(cls, id):
        return Curses.get_or_none(id)

    # Изменение названия курса
    @classmethod
    def update_curs(cls, id, new_name):
        Curses.update(curs = new_name).where(Curses.id == id).execute()

    # Удаление курса
    @classmethod
    def delete_curs(cls, id):
        Curses.delete().where(Curses.id == id).execute()

if __name__ == "__main__":
    Curs_Controllers.add_curs("Test Curs")