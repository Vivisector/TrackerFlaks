from datetime import datetime
from extensions import db


class Task(db.Model):
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
