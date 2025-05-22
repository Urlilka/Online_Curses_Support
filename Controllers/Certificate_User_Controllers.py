from Models.Certificates import *
from Models.Users import *
from Models.Certifications_Users import *

class Certificate_User_Controllers():

    # Добавление ассоциации Сертификат <---> Пользователь
    @classmethod
    def add_certificate_to_user(cls,certificate_id, user_id):
        Certificates_Users.create(
            certificate_id = certificate_id,
            user_id = user_id
        )

    # Удаление ассоциации Сертификат <---> Пользователь
    @classmethod
    def delete_certificate_to_user(cls, id):
        Certificates_Users.delete().where(Certificates_Users.id == id).execute()
