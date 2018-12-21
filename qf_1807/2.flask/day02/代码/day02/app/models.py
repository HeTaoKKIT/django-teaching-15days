
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(80), unique=True, nullable=False)
    s_age = db.Column(db.Integer, default=1)

    __tablename__ = 'stu'
