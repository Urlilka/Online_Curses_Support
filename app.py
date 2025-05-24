from crypt import methods

from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

from Controllers.User_Controllers import User_Controller
from Models.Users import Users

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = "00000"

@login_manager.user_loader
def load_user(user_id):
    return User_Controller.show(int(user_id))

# Метод выхода
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

# Перенаправление неавторизованных в корень
@login_manager.unauthorized_handler
def unauthorized():
    if not current_user.is_authenticated:
        return redirect("/")

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

@app.route("/student_panel")
@login_required
def student():
    title = f"Панель студента. Группа {Users.role_id.role}"
    if current_user.role_id.role == "Student":
        pass
    return render_template(
        "stud_panel.html",
        title = title
    )

if __name__ == "__main__":
    # Запуск переменной app и веб-сервер
    app.run(debug=True)