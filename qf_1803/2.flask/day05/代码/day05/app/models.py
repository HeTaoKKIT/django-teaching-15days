
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(10), nullable=False)
    s_age = db.Column(db.Integer, nullable=True)
    s_create_time = db.Column(db.DateTime)
    g_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=True)

    __tablename__ = 'student'

    def __init__(self, name, age):
        self.s_name = name
        self.s_age = age
        self.s_create_time = datetime.now()

    def save_update(self):
        db.session.add(self)
        db.session.commit()


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), nullable=False)
    g_create_time = db.Column(db.DateTime, default=datetime.now)
    stu = db.relationship('Student', backref='grade', lazy=True)


c_s = db.Table('stu_course',
               db.Column('s_id',
                         db.Integer,
                         db.ForeignKey('student.id'),
                         primary_key=True),
               db.Column('c_id',
                         db.Integer,
                         db.ForeignKey('course.id'),
                         primary_key=True)
               )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(10), nullable=False)
    c_desc = db.Column(db.String(20), nullable=True)
    stu = db.relationship('Student', secondary=c_s, backref='course')

    __tablename__ = 'course'


