
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    icon = db.Column(db.String(100), nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()