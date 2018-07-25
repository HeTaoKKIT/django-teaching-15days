
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), nullable=False)
    s_age = db.Column(db.Integer, nullable=True)
    s_create_time = db.Column(db.DateTime)

    __tablename__ = 'student'


