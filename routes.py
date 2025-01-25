from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models import Task

bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    """
    Главная страница приложения.

    Метод: GET
    URL: /

    Описание:
        Получает список всех задач из базы данных и отображает их на главной странице.

    Возвращает:
        - HTML-страницу с отображением списка задач.
    """
    tasks = Task.query.all()  # Получаем все задачи
    return render_template('index.html', tasks=tasks)


@bp.route('/task/new', methods=['GET', 'POST'])
def create_task():
    """
    Создание новой задачи.

    Методы: GET, POST
    URL: /task/new

    Описание:
        - GET: Отображает форму для создания новой задачи.
        - POST: Обрабатывает данные формы и создает новую задачу в базе данных.

    Поля формы (POST):
        - title: Заголовок задачи (обязательное поле).
        - description: Описание задачи.
        - progress: Прогресс задачи (по умолчанию 0).

    Возвращает:
        - GET: HTML-страницу с формой создания задачи.
        - POST: Перенаправление на главную страницу после создания задачи.
    """
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        progress = request.form.get('progress', 0)

        task = Task(
            title=title,
            description=description,
            progress=progress
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template('create_task.html')


@bp.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    """
    Редактирование существующей задачи.

    Методы: GET, POST
    URL: /task/<int:task_id>/edit

    Описание:
        - GET: Отображает форму для редактирования задачи.
        - POST: Обновляет данные задачи в базе данных.

    Параметры URL:
        - task_id (int): ID задачи, которую нужно отредактировать.

    Поля формы (POST):
        - title: Новый заголовок задачи.
        - description: Новое описание задачи.
        - progress: Новый прогресс задачи.
        - status: Новый статус задачи (по умолчанию "in progress").

    Возвращает:
        - GET: HTML-страницу с формой редактирования задачи.
        - POST: Перенаправление на главную страницу после сохранения изменений.
    """
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.progress = int(request.form.get('progress', 0))
        task.status = request.form.get('status', 'in progress')

        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template('edit_task.html', task=task)


@bp.route('/task/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    """
    Завершение задачи.

    Метод: POST
    URL: /task/<int:task_id>/complete

    Описание:
        Устанавливает прогресс задачи на 100% и статус как "done".

    Параметры URL:
        - task_id (int): ID задачи, которую нужно завершить.

    Возвращает:
        Перенаправление на главную страницу после завершения задачи.
    """
    task = Task.query.get_or_404(task_id)
    task.progress = 100
    task.status = 'done'
    db.session.commit()
    return redirect(url_for('routes.index'))


@bp.route('/task/<int:id>/delete', methods=['POST'])
def delete_task(id):
    """
    Удаление задачи.

    Метод: POST
    URL: /task/<int:id>/delete

    Описание:
        Удаляет задачу из базы данных.

    Параметры URL:
        - id (int): ID задачи, которую нужно удалить.

    Возвращает:
        Перенаправление на главную страницу после удаления задачи.
    """
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('routes.index'))
