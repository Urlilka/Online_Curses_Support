from Models.Certificates import *

class Certificate_Controllers():

    # Добавление Сертификата
    @classmethod
    def add_certificate(cls, cert_link):
        Certificates.create(cert_link = cert_link)

    # Вывод всех сертификатов
    @classmethod
    def get_certificates(cls):
        return Certificates.select().order_by(Certificates.id.asc())

    # Изменение Сертификата
    @classmethod
    def update_test(cls, id, new_link):
        Certificates.update(cert_link = new_link).where(Certificates.id == id).execute()

    # Удаление Сертификата
    @classmethod
    def delete_test(cls, id):
        Certificates.delete().where(Certificates.id == id).execute()

if __name__ == "__main__":
    Certificate_Controllers.add_certificate("https://google.com")