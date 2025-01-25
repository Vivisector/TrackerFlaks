from datetime import datetime
from extensions import db


class Task(db.Model):
    """
    Модель для представления задачи в системе.

    Назначение:
        Содержит информацию о задаче, включая заголовок, описание, статус и прогресс выполнения.

    Поля:
        - id (int): Уникальный идентификатор задачи.
        - title (str): Заголовок задачи (обязательное поле, до 120 символов).
        - description (str): Описание задачи (необязательное, до 500 символов).
        - created_at (datetime): Дата и время создания задачи (по умолчанию - текущее время).
        - updated_at (datetime): Дата и время последнего обновления (обновляется автоматически).
        - status (str): Статус задачи (по умолчанию - 'pending', другие варианты: 'done').
        - progress (int): Прогресс выполнения задачи (от 0 до 100, по умолчанию - 0).

    Методы:
        - __repr__: Возвращает строковое представление задачи.
    """
    __tablename__ = 'tasks_task'  # Укажите имя таблицы явно
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # pending, done
    progress = db.Column(db.Integer, nullable=True, default=0)  # Добавьте поле progress

    def __repr__(self):
        return f'<Task {self.title}>'

