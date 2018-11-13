
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 第一步: 声明模型


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=True)

    __tablename__ = 'day02_user'


