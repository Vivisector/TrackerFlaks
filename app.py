import os
from flask import Flask
from flask import request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from models import Task
from extensions import db


def create_app():
    """
    Создает и настраивает экземпляр приложения Flask.

    Функция выполняет следующие действия:
        - Создает объект Flask-приложения.
        - Конфигурирует базу данных (SQLAlchemy) с использованием SQLite.
        - Инициализирует базу данных.
        - Регистрирует маршруты через Blueprint.

    Возвращает:
        Flask: Экземпляр приложения Flask.
    """
    # Создаем приложение Flask
    app = Flask(__name__)
    # Настройки для базы данных
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.abspath("db.sqlite3")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализируем базу данных с приложением
    db.init_app(app)

    # Регистрируем Blueprint
    from routes import bp
    app.register_blueprint(bp)
    # Импортируем модели после инициализации базы данных
    # from models import Task  # Импортируем модели после того как db проинициализирован

    return app

# if __name__ == '__main__':
#     app.run(debug=True)
