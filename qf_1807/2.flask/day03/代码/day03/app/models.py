
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'student' # 默认表名就为student
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True, nullable=False)
    s_phone = db.Column(db.String(11), nullable=True)
    s_age = db.Column(db.Integer, nullable=False)
    s_gender = db.Column(db.Integer, default=1)


