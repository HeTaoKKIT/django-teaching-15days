
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'student' # 默认表名就为student
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True, nullable=False)
    s_phone = db.Column(db.String(11), nullable=True)
    s_age = db.Column(db.Integer, nullable=False)
    s_gender = db.Column(db.Integer, default=1)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=True)


class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), unique=True, nullable=False)
    stus = db.relationship('Student', backref='g')


s_c = db.Table('s_c',
  db.Column('s_id', db.Integer, db.ForeignKey('student.id')),
  db.Column('c_id', db.Integer, db.ForeignKey('course.id'))
    )


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(10), unique=True, nullable=False)
    stus = db.relationship('Student', secondary=s_c, backref='cou', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()