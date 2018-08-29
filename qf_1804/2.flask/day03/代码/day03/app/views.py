import random

from flask import Blueprint, render_template, request, \
    redirect, url_for
from sqlalchemy import desc, asc, and_, not_, or_

from app.models import db, Student

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