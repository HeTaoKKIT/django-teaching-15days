
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), unique=True, nullable=False)
    gender = db.Column(db.Boolean, default=1)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=True)

    # __tablename__用于指定模型映射的表名，如果没有指定，则表名为模型名的小写

    def save(self):
        db.session.add(self)
        db.session.commit()


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), nullable=False, unique=True)
    student = db.relationship('Student', backref='g')


