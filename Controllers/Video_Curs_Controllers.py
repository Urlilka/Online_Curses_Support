from Models.Videos import *
from Models.Curses import *
from Models.Videos_Curses import *

class Video_Curs_Controllers():

    # Создание записи с ассоциацией Курс <---> Видео
    @classmethod
    def add_video_to_curs(cls, video_id, curs_id):
        Videos_Curses.create(
            video_id = video_id,
            curs_id = curs_id
        )

    @classmethod
    # Удаление записи с ассоциацией Курс <---> Видео
    def delete_video_to_curs(cls, id):
        Videos_Curses.delete().where(Videos_Curses.id == id).execute()
