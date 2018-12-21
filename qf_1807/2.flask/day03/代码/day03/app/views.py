import random

from flask import Blueprint, render_template, request, \
    redirect, url_for
from sqlalchemy import and_, not_, or_

from app.models import Student, db


blue = Blueprint('app', __name__)


@blue.route('/')
def hello():
    return 'hello'


@blue.route('/list/', methods=['GET'])
def stu_list():
    # students = Student.query.all()
    # 127.0.0.1:8080/app/list/?page=3
    page = int(request.args.get('page', 1))
    pre_page = 5
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
