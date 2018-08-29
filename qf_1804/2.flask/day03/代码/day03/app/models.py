
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), unique=True)
    s_age = db.Column(db.Integer, default=10)

    __tablename__ = 'student'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, name, age):
        # 2
        self.s_name = name
        self.s_age = age
