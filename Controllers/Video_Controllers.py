from Models.Videos import *

class Video_Controllers():

    # Добавление Видео
    @classmethod
    def add_video(cls, video_link):
        return Videos.create(video_link = video_link)

    # Вывод всех видео
    @classmethod
    def get_videos(cls):
        return Videos.select().order_by(Videos.id.asc())

    # Изменение Видео
    @classmethod
    def update_video(cls, id, new_link):
        Videos.update(video_link = new_link).where(Videos.id == id).execute()

    # Удаление Видео
    @classmethod
    def delete_video(cls, id):
        Videos.delete().where(Videos.id == id).execute()
