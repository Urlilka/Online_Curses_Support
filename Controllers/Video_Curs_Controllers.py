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

    # Получение связанных данных с курсом <--> Видео
    @classmethod
    def get_student_curs_video(cls, curs_id):
        return Videos.select().join(Videos_Curses).where(Videos_Curses.curs_id == curs_id)

    @classmethod
    # Удаление записи с ассоциацией Курс <---> Видео
    def delete_video_to_curs(cls, id):
        Videos_Curses.delete().where(Videos_Curses.id == id).execute()

if __name__ == "__main__":
    # Video_Curs_Controllers.add_video_to_curs(1,1)
    for row in Video_Curs_Controllers.get_student_curs_video(1):
        print(row.video_link)