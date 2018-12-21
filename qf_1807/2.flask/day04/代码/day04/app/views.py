import random

from flask import Blueprint, render_template, request, \
    redirect, url_for, abort, g
from sqlalchemy import and_, not_, or_

from app.models import Student, db, Grade, Course

import pymysql

blue = Blueprint('app', __name__)


@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@blue.route('/')
def hello():
    return 'hello'


@blue.route('/list/', methods=['GET'])
def stu_list():
    # students = Student.query.all()
    # 127.0.0.1:8080/app/list/?page=3
    page = int(request.args.get('page', 1))
    pre_page = 1
    paginate = Student.query.paginate(page, pre_page)
    students = paginate.items
    return render_template('list.html',
                           students=students,
                           paginate=paginate
                           )


@blue.route('/add/', methods=['GET', 'POST'])
def stu_add():
    if request.method == 'GET':
        return render_template('add.html')

    if request.method == 'POST':
        # 创建学生信息
        # 1. 获取数据
        username = request.form.get('username')
        phone = request.form.get('phone')
        age = request.form.get('age')
        # 2. 保存
        stu = Student()
        stu.s_name = username
        stu.s_age = age
        stu.s_phone = phone
        db.session.add(stu)
        db.session.commit()
        return redirect(url_for('app.stu_list'))


@blue.route('/edit/<int:id>/', methods=['GET', 'POST'])
def stu_edit(id):
    if request.method == 'GET':
        stu = Student.query.filter(Student.id == id).first()
        return render_template('add.html', stu=stu)

    if request.method == 'POST':
        # 1. 获取页面中的参数
        username = request.form.get('username')
        phone = request.form.get('phone')
        age = request.form.get('age')
        # 2. 获取对象
        stu = Student.query.filter(Student.id == id).first()
        # 3. 修改属性
        stu.s_name = username
        stu.s_phone = phone
        stu.s_age = age
        db.session.add(stu)
        db.session.commit()
        return redirect(url_for('app.stu_list'))


@blue.route('/del/<int:id>/', methods=['GET'])
def stu_del(id):
    # 1. 获取删除的对象
    stu = Student.query.filter(Student.id == id).first()
    # 2. 使用delete(对象)
    db.session.delete(stu)
    db.session.commit()
    return redirect(url_for('app.stu_list'))


@blue.route('/add_all/', methods=['GET'])
def add_all():
    stus = []
    for i in range(10):
        stu = Student()
        stu.s_age = random.randint(18, 28)
        stu.s_name = '小明%s' % random.randint(0,10000)
        stu.s_phone = '12334456743'
        stus.append(stu)
        # db.session.add(stu)
    db.session.add_all(stus)
    db.session.commit()
    return '创建成功'


@blue.route('/change_stu/', methods=['GET'])
def change_stu():
    stu = Student.query.filter(Student.id == 3).first()
    stu.s_name = '小花121212'
    # db.session.add(stu)
    db.session.commit()
    return '修改成功'


@blue.route('/sel_stu/', methods=['GET'])
def sel_stu():
    # 查询id=3的信息
    stu = Student.query.filter(Student.id == 3).first()
    stu = Student.query.filter_by(id=3).first()
    stu = Student.query.get(3)
    # 查询所有数据
    # all()返回所有数据的列表结果
    stus = Student.query.all()
    # 排序
    stus = Student.query.order_by('s_age')
    stus = Student.query.order_by('-s_age')
    stus = Student.query.order_by('s_age asc')
    stus = Student.query.order_by('s_age desc')
    # 实现分页
    stus = Student.query.offset(0).limit(2)

    # 模糊查询contains
    stus = Student.query.filter(Student.s_name.contains('小花')).all()
    # 以小开头的学生信息， startswith
    stus = Student.query.filter(Student.s_name.startswith('小')).all()
    # 以3结尾的学生信息, endswith
    stus = Student.query.filter(Student.s_name.endswith('3')).all()
    # 第二位为’明‘的学生信息， like ’_明%‘
    stus = Student.query.filter(Student.s_name.like('_明%')).all()

    # 查询id为1,2,3,4,5的学生信息
    stus = Student.query.filter(Student.id.in_([1,2,3,4,5]))

    # 年龄。查询年龄小于21的信息
    # lt le  gt  ge
    stus = Student.query.filter(Student.s_age.__le__(21)).all()
    stus = Student.query.filter(Student.s_age <= 21).all()

    # 查询年龄小于22，且姓名以6结束
    stus = Student.query.filter(Student.s_age < 22).\
        filter(Student.s_name.endswith('6')).all()

    stus = Student.query.filter(Student.s_age < 22,
                                Student.s_name.endswith('6')).all()

    # and_
    stus = Student.query.filter(and_(Student.s_age < 22,
                                     Student.s_name.endswith('6')
                                     )
                                ).all()

    # or_
    stus = Student.query.filter(or_(Student.s_age < 22,
                                     Student.s_name.endswith('6')
                                     )
                                ).all()
    # not_
    stus = Student.query.filter(not_(Student.s_age == 22)).all()

    # 分页
    stus = Student.query.paginate(1, 5)

    names = [stu.s_name for stu in stus]
    print(names)
    return '查询成功'


@blue.route('/add_grade/')
def add_grade():
    # 批量添加班级信息， add_all
    g_list = []
    grades = ['Python', 'Java', 'Php', 'C++', 'C', 'Ruby', 'Go', '易语言', 'lua']
    for grade in grades:
        g = Grade()
        g.g_name = grade
        g_list.append(g)
    db.session.add_all(g_list)
    db.session.commit()
    return '创建班级成功'


@blue.route('/stu_gra/')
def stu_grade():
    # 给id为3,4,5的学生分配到python班
    stus = Student.query.filter(Student.id.in_([3,4,5])).all()
    for stu in stus:
        stu.grade_id = 1
        db.session.add(stu)
    db.session.commit()
    return '分配班级成功'


@blue.route('/sel_stu_by_grade/', methods=['GET'])
def sel_stu_by_grade():
    # 通过班级查找学生
    # 查询python班级的学生信息
    grade = Grade.query.filter(Grade.g_name=='Python').first()
    students = grade.stus
    return '查询成功'


@blue.route('/sel_grade_by_stu/', methods=['GET'])
def sel_grade_by_stu():
    # 查询id=12的学生对于的班级信息
    stu = Student.query.get(12)
    grade = stu.g
    return '学生查询班级成功'

# 多对多


@blue.route('/add_cou/', methods=['GET'])
def add_cou():
    cous = ['线代', '高数', '概论', '大学物理', '大学英语']
    for cou in cous:
        c = Course()
        c.c_name = cou
        c.save()
    return '创建课程成功'


@blue.route('/add_s_c/', methods=['GET'])
def add_s_c():
    # 给id=3的学生选择线代这门课
    stu = Student.query.get(3)
    cou = Course.query.filter(Course.c_name=='线代').first()
    # 学生查询课程
    # stu.cou
    # 课程查询学生
    # cou.stus
    # 学生添加课程
    # stu.cou.append(cou)
    # 课程添加学生
    #cou.stus.append(stu)
    # 学生删除某门课
    # stu.cou.remove(cou)
    # db.session.commit()
    return '添加学生课程'

###################################

# 钩子函数


@blue.before_request
def before_req():
    print('请求之前执行代码1')


@blue.before_request
def before_req1():
    print('请求之前执行代码2')


@blue.route('/index/')
def index():
    # 10/0
    a = 1
    b = 0
    a/b
    # try:
    #     a/b
    return '我是index'
    # except:
    #     # 抛出异常
    #     abort(404)


@blue.after_request
def after_req(response):
    print('请求之后执行的代码3')
    return response


@blue.after_request
def after_req1(response):
    print('请求之后执行的代码4')
    return response


@blue.teardown_request
def teardown_request(exception):
    print('teardown request')
    return exception


# @blue.errorhandler(500)
# def error(e):
#     print(e)
#     return e

# 连接数据库

# @blue.before_request
# def before_req():
#     conn = pymysql.Connection(host='127.0.0.1', port=3306,
#                        database='flask7', user='root',
#                        password='123456')
#     cursor = conn.cursor()
#     g.cursor = cursor
#     g.conn = conn
#
#
# @blue.route('/my_sel_stu/')
# def my_sel_stu():
#     sql = 'select * from student;'
#     g.cursor.execute(sql)
#     data = g.cursor.fetchall()
#     return '查询成功'
#
#
# @blue.teardown_request
# def teardown_req(e):
#     g.conn.close()
#     return e


