from Controllers.Certificate_Controllers import Certificate_Controllers
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

    @classmethod
    def get_student_cert_user(cls,user_id):
        return Certificates_Users.select().where(Certificates_Users.user_id == user_id)

    # Удаление ассоциации Сертификат <---> Пользователь
    @classmethod
    def delete_certificate_to_user(cls, id):
        Certificates_Users.delete().where(Certificates_Users.id == id).execute()

if __name__ == "__main__":
    # Certificate_User_Controllers.add_certificate_to_user(2,7)
    for row in Certificate_User_Controllers.get_student_cert_user(7):
        print(row.certificate_id.id, row.certificate_id.cert_link)