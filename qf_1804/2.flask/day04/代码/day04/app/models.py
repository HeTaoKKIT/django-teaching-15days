
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), unique=True)
    s_age = db.Column(db.Integer, default=10)
    s_g = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=True)

    __tablename__ = 'student'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, name, age):
        # 2
        self.s_name = name
        self.s_age = age


class Grade(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    g_name = db.Column(db.String(10), unique=True)
    student = db.relationship('Student', backref='stu', lazy=True)


s_c = db.Table('s_c',
               db.Column('s_id', db.Integer, db.ForeignKey('student.id')),
               db.Column('c_id', db.Integer, db.ForeignKey('course.id'))
               )


class Course(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    c_name = db.Column(db.String(10), unique=True)
    student = db.relationship('Student', secondary=s_c, backref='cou')

