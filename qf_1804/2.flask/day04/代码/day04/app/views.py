import random

from flask import Blueprint, render_template, request, \
    redirect, url_for
from sqlalchemy import desc, asc, and_, not_, or_
from flask_restful import Resource

from app.models import db, Student, Grade, Course
from utils import api

blue = Blueprint('app', __name__)


@blue.route('/')
def hello():
    return 'hello'


@blue.route('create_db/')
def create_db():
    # 创建数据中的表
    db.create_all()
    return '创建数据表成功'


@blue.route('drop_db/')
def drop_db():
    # 删除数据中的表
    db.drop_all()
    return '删除数据表成功'


@blue.route('create_stu/')
def create_stu():
    # 创建学生信息
    stu = Student()
    stu.s_name = '小明1'
    stu.s_age = 18
    # # 第一种：直接保存数据
    # db.session.add(stu)
    # # 事务：完整，一致，持久，原子
    # db.session.commit()

    # 第二种：自定义save()方法
    stu.save()
    return '创建学生信息成功'


@blue.route('sel_stu/')
def sel_stu():
    # 查询所有操作
    students = Student.query.all()
    # 第一种方式：查询id=1的学生信息
    students = Student.query.filter(Student.id==1)
    # 第二种方式：查询id=1的学生信息
    students = Student.query.filter_by(id=1)
    # 第三种方式：查询id=1的学生信息
    sql = 'select * from student where id=1;'
    students = db.session.execute(sql)
    # 查询所有学生数据
    sql = 'select * from student;'
    students = db.session.execute(sql)

    # 模糊查询, 查询姓名中包含妲己的学生信息
    # 在django中 filter(s_name__contains='妲己')
    # 语法：filter(模型名.属性.运算符('xx'))
    students = Student.query.filter(Student.s_name.contains('妲己'))
    # 以什么开始，startswith
    students = Student.query.filter(Student.s_name.startswith('校'))
    # 以什么结束，endswith
    students = Student.query.filter(Student.s_name.endswith('9'))
    # 查询年龄大于等于16的学生信息
    students = Student.query.filter(Student.s_age.__ge__(16))
    # 查询id在10到12之间的学生信息
    students = Student.query.filter(Student.id.in_([10,11,12]))
    # 查询年龄小于15的学生信息
    students = Student.query.filter(Student.s_age.__lt__(15))
    # 模糊查询，使用like，查询姓名中第二位为花的学生信息
    # like '_花%'
    students = Student.query.filter(Student.s_name.like('_花%'))
    # 按照id降序,升序
    students = Student.query.order_by('id')
    students = Student.query.order_by('-id')

    students = Student.query.order_by(desc('id'))
    students = Student.query.order_by(asc('id'))

    students = Student.query.order_by('id desc')
    students = Student.query.order_by('id asc')

    # 查询数据，获取第五个到第十个的数据
    students = Student.query.all()[4:10]
    page = 3
    students = Student.query.offset((page-1) * 2).limit(2)
    # 使用get，获取id=1的学生信息
    # get拿不到值，不会报错，只会返回一个空
    students = Student.query.get(1)

    # and_, not_, or_
    students = Student.query.filter(Student.s_age==16,
                                    Student.s_name.contains('花'))

    students = Student.query.filter(and_(Student.s_age==16,
                                         Student.s_name.contains('花')))
    students = Student.query.filter(not_(Student.s_age == 16),
                                    not_(Student.s_name.contains('花')))

    students = Student.query.filter(or_(Student.s_age == 16,
                                         Student.s_name.contains('花')))

    # 查询年龄小于15的学生信息
    students = Student.query.filter(Student.s_age < 15)
    students = Student.query.filter(Student.s_age.__lt__(15))

    return render_template('stus.html', stus=students)


@blue.route('del_stu/<int:id>/', methods=['GET'])
def del_stu(id):
    # 删除学生
    if request.method == 'GET':
        stu = Student.query.filter(Student.id==id).first()
        db.session.delete(stu)
        db.session.commit()
        return '删除学生成功'


@blue.route('edit_stu/<int:id>/', methods=['GET', 'POST'])
def edit_stu(id):
    if request.method == 'GET':
        stu = Student.query.filter_by(id=id).first()
        return render_template('edit.html', stu=stu)
    if request.method == 'POST':
        username = request.form.get('username')
        age = request.form.get('age')
        # 更新,第一种
        # stu = Student.query.filter_by(id=id).first()
        # stu.s_name = username
        # stu.s_age = age
        # stu.save()
        # 更新第二种
        Student.query.filter_by(id=id).update({'s_name': username, 's_age': age})
        db.session.commit()

        return redirect(url_for('app.sel_stu'))


@blue.route('create_many_stu/', methods=['GET'])
def create_many_stu():
    if request.method == 'GET':
        # 批量添加学生信息
        stus_list = []
        for i in range(10):
            stu = Student()
            stu.s_name = '校花%s' % random.randrange(10,10000)
            stu.s_age = 16
            stus_list.append(stu)
        # add_all()添加学生信息，参数为列表，列表中为添加的学生对象
        db.session.add_all(stus_list)
            # db.session.add(stu)
        db.session.commit()
        return '批量创建'


@blue.route('create_many_stu_init/', methods=['GET'])
def create_many_stu_init():
    if request.method == 'GET':
        stu_list = []
        for i in range(10):
            stu = Student('小花%s' % random.randrange(10,10000), 10)
            stu_list.append(stu)
        db.session.add_all(stu_list)
        db.session.commit()
        return '批量创建成功'


@blue.route('paginate/', methods=['GET'])
def stu_paginate():
    # 实现分页
    # 1. 使用offset+limit实现
    page = int(request.args.get('page', 1))
    stus = Student.query.offset((page - 1)*5).limit(5)
    # 2. 使用切片实现
    stus = Student.query.all()[(page - 1)*5:page*5]
    # 3. 使用paginate实现
    paginate = Student.query.paginate(page, 10)
    stus = paginate.items
    return render_template('stus.html', stus=stus, paginate=paginate)


# 创建班级， add()， add_all()
@blue.route('create_grade/', methods=['GET'])
def create_grade():
    grade_name = ['Python', 'Java', 'Php', 'VHDL']
    g_list = []
    for name in grade_name:
        grade = Grade()
        grade.g_name = name
        g_list.append(grade)
        # db.session.add(grade)
        # db.session.commit()
    db.session.add_all(g_list)
    db.session.commit()

    return '创建班级成功'

# 添加班级和学生信息关联关系

@blue.route('sel_grade_by_stu/', methods=['GET'])
def sel_grade_by_stu():
    if request.method == 'GET':
        # 查询id=4的学生，对应的班级
        # 1. 获取id=4的学生信息
        stu = Student.query.get(4)
        # 2. 使用关联关系，relationship中的backref去反向查询班级信息
        grade = stu.stu
        return 'id为%s的学生的班级为：%s' % (4, grade.g_name)


@blue.route('sel_stu_by_grade/', methods=['GET'])
def sel_stu_by_grade():
    if request.method == 'GET':
        # 查询java班中的学生信息
        grade = Grade.query.filter(Grade.g_name=='Java').first()
        # 班级对象.relationship的字段
        students = grade.student
        return '查询成功'

# 添加课程信息
@blue.route('add_course/', methods=['GET'])
def add_course():
    if request.method == 'GET':
        courses = ['线代', '高数', '大学物理', '计算机', '英语']
        for course in courses:
            c = Course()
            c.c_name = course
            db.session.add(c)
        db.session.commit()
        return '创建课程成功'


@blue.route('add_stu_course/', methods=['GET'])
def add_stu_course():
    if request.method == 'GET':
        # id=4的学生选择了三门课程(id=1,2,3)
        stu = Student.query.get(4)
        c1 = Course.query.get(1)
        c2 = Course.query.get(2)
        c3 = Course.query.get(3)
        stu.cou.append(c1)
        stu.cou.append(c2)
        stu.cou.append(c3)
        db.session.add(stu)
        db.session.commit()
        return '添加学生的课程成功'


@blue.route('del_stu_course/', methods=['GET'])
def del_stu_course():
    if request.method == 'GET':
        stu = Student.query.get(4)
        cou = Course.query.get(1)
        # 删除列表中数据
        stu.cou.remove(cou)
        # del stu.cou[0]
        db.session.add(stu)
        db.session.commit()
        return '删除学生的课程成功'


class StudentResource(Resource):

    def get(self, id):
        stu = Student.query.get(id)
        return {'s_name': stu.s_name, 's_age': stu.s_age}

    def post(self, id):
        pass

    def put(self):
        pass

    def patch(self, id):
        s_name = request.form.get('s_name')
        stu = Student.query.get(id)
        stu.s_name = s_name
        db.session.add(stu)
        db.session.commit()
        return {'code': 200, 'msg': '请求成功'}

    def delete(self):
        pass

api.add_resource(StudentResource, '/api/student/<int:id>/')
