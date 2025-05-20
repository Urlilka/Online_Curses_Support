from Models.Tests_Curses import *
from Models.Videos_Curses import *
from Models.Curses_Users import *
from Models.Curses import *
from Models.Users import *
from Models.Videos import *
from Models.Tests import *

class User_curs_Controllers():

    # Получение связанных данных с пользователем <---> курсом
    @classmethod
    def get_student_curs(cls, user_id):
        return Curses.select().join(Curses_Users).where(Curses_Users.user_id == user_id)