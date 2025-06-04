from crypt import methods
from flask import Flask, render_template, request, url_for, jsonify
from werkzeug.utils import redirect
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

from Controllers.Certificate_User_Controllers import Certificate_User_Controllers
from Controllers.Recomendation_User_Controllers import Recomendation_User_Controllers
from Controllers.Test_Curs_Controllers import Test_Curs_Controllers
from Controllers.User_Controllers import User_Controller
from Controllers.User_Curs_Controllers import User_curs_Controllers
from Controllers.Video_Curs_Controllers import Video_Curs_Controllers
from Models.Users import Users


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = "00000"

# ---------------------------------------------------------------------
# Активный пользователь
@login_manager.user_loader
def load_user(user_id):
    return User_Controller.show(int(user_id))
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Метод выхода
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Перенаправление неавторизованных в корень
@login_manager.unauthorized_handler
def unauthorized():
    if not current_user.is_authenticated:
        return redirect("/")
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Корень сайта / Главная страница
@app.route("/", methods = ['POST','GET'])
def login():
    # Титульник а base.html
    title = "Вход"
    # Передача в переменые строки из форм
    login = request.form.get('login')
    password = request.form.get('password')
    # Проверка
    if request.method == "POST":
        if User_Controller.auth(login,password):
            user = User_Controller.show_login(login)
            login_user(user)
            if current_user.role_id.role == "Admin":
                return redirect("/admin_panel")
                # print("ADMIN VK JIVET IN .....")
            else:
                return redirect("/student_panel")
                # print("STUDENT")
        else:
            print("Nope nope!!!")
    return render_template("index.html", title=title)
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Панель студента
@app.route("/student_panel")
@login_required
def student():
    if current_user.role_id.role == "Student":
        title = f"Панель студента. Группа {User_curs_Controllers.get_curs_from_user(current_user.id).curs_id.curs}"
        video = Video_Curs_Controllers.get_student_curs_video(User_curs_Controllers.get_curs_from_user(current_user.id).curs_id)
        test = Test_Curs_Controllers.get_student_curs_test(User_curs_Controllers.get_curs_from_user(current_user.id).curs_id)
        group = User_curs_Controllers.get_curs_from_user(current_user.id).curs_id.curs
        name = User_Controller.show(current_user.id).firstname + " " + User_Controller.show(current_user.id).surname
        # for row in test:
        #     print(row.test_id.test_link)
        # print(group)
        return render_template(
            "stud_panel.html",
            title = title,
            video = video,
            test = test,
            group = group,
            name = name
        )
    else:
        return redirect("/logout")
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Отслеживание ссылок видео
@app.route("/track_link_left", methods=["POST"])
def track_link_left():
    data = request.get_json()
    link_id = data["link_id"]
    action = data["action"]
    print(f"Клик по сылке: {link_id} | действие {action}")
    return jsonify(success=True)
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Отслеживание ссылок теста
@app.route("/track_link_right", methods=["POST"])
def track_link_right():
    data = request.get_json()
    link_id_2 = data["link_id_2"]
    action = data["action"]
    print(f"Клик по сылке: {link_id_2} | действие {action}")
    return jsonify(success=True)
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Панель сертификатов
# @app.route("/student_panel/certifications/<int:id>")
@app.route("/student_panel/certifications")
@login_required
def certificate():
    if current_user.role_id.role == "Student":
        title = f"Cертификаты студента. Группа {User_curs_Controllers.get_curs_from_user(current_user.id).curs_id.curs}"
        group = User_curs_Controllers.get_curs_from_user(current_user.id).curs_id.curs
        name = User_Controller.show(current_user.id).firstname + " " + User_Controller.show(current_user.id).surname
        cert = Certificate_User_Controllers.get_student_cert_user(current_user.id)
        return render_template(
            "cert_panel.html",
            title = title,
            name = name,
            group = group,
            cert = cert
        )
    else:
        return redirect("/logout")
# ---------------------------------------------------------------------

# Панель Рекомендаций
# @app.route("/student_panel/recomendations/<int:id>")
@app.route("/student_panel/recomendations")
@login_required
def recomendate():
    if current_user.role_id.role == "Student":
        title = f"Рекомендации студента. Группа {User_curs_Controllers.get_curs_from_user(current_user.id).curs_id.curs}"
        group = User_curs_Controllers.get_curs_from_user(current_user.id).curs_id.curs
        name = User_Controller.show(current_user.id).firstname + " " + User_Controller.show(current_user.id).surname
        recom = Recomendation_User_Controllers.get_student_recom_user(current_user.id)

        return render_template(
            "recom_panel.html",
            title = title,
            group = group,
            name = name,
            recom = recom
        )
    else:
        return redirect("/logout")
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Запуск переменной app и веб-сервера
if __name__ == "__main__":

    app.run(debug=True)

# ---------------------------------------------------------------------