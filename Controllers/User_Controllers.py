from Models.Users import *
from bcrypt import hashpw, gensalt, checkpw

class User_Controller:

    # Регистрация пользователя (В role_id == 1 --- Admin, 2 --- Student)
    @classmethod
    def registration(cls, username, password, firstname, surname, role_id):
        # Хэшируем пароль
        hash_password = hashpw(password.encode("utf-8"), gensalt())
        # Создаём пользователя
        Users.create(username = username, password = hash_password, firstname = firstname, surname = surname, role_id = role_id)

    # Проверка логина и пароля (Аунтефикация(Вход))
    @classmethod
    def auth(cls,username, password):
        # проверяем логин. В случае успеха проверяем пароль
        if Users.get_or_none(Users.username == username) != None:
            hspassword = Users.get_or_none(Users.username == username).password
            if checkpw(password.encode('utf-8'),hspassword.encode('utf-8')):
                return True
        return False

    # Вывод записей из таблицы
    @classmethod
    def get(cls):
        return Users.select()

    # Удалить
    @classmethod
    def delete(cls, *id):
        for user in id:
            Users.delete_by_id(user)

    # Обновление записи
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            if key == "password":
                value = hashpw(value.encode("utf-8"), gensalt())
            Users.update({key:value}).where(Users.id == id).execute()

    # Вывод одной записи
    @classmethod
    def show(cls, id):
        return Users.get_or_none(id)

    # Вывод одного пользователя по логину
    @classmethod
    def show_login(cls,login):
        return Users.get_or_none(Users.username == login)

if __name__ == "__main__":
    # User_Controller.registration("student","student","student_name","student_surname",2)

    print(User_Controller.auth("student","student"))

    for i in User_Controller.get():
        print(i.id,i.username,i.password,i.firstname,i.surname,i.role_id.role)

    # print(Users.get_or_none(Users.username == "admin").password)