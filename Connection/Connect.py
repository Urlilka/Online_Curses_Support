from peewee import *

# Подключение к БД

def connect():
    mysql_db = MySQLDatabase(
        "GilAisp2_Curs_Supp",
        user = "GilAisp2_Admin",
        password = "000000",
        host = "10.11.13.118",
        port = 3306
    )
    return mysql_db


if __name__ == "__main__":
    print(connect().connect())