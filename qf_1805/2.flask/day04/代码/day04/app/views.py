
from flask import Blueprint, request, render_template

from app.models import db, Students, Grade, Course

blue = Blueprint('app', __name__)


@blue.route('/')
def hello():
    return 'hello'


@blue.route('/create_db/')
def create_db():
    # 用于初次创建模型
    db.create_all()
    return '创建成功'


@blue.route('/drop_db/')
def drop_db():
    # 删除数据库中所有的表
    db.drop_all()
    return '删除成功'


@blue.route('/create_stu/')
def create_stu():
    # 实现创建， add()
    stu = Students()
    stu.s_name = '小明1'
    stu.save()
    return '创建学生信息成功'


@blue.route('/create_stu_all/')
def create_stu_all():
    # 批量创建，add_all()
    names = ['小王', '老王', '厂长', '莉哥', '温婉']
    stu_list = []
    for name in names:
        stu = Students()
        stu.s_name = name
        # stu.save()
        stu_list.append(stu)
        # db.session.add(stu)
    db.session.add_all(stu_list)
    db.session.commit()
    return '批量创建成功'


@blue.route('/sel_stu/')
def sel_stu():
    # 查询， filter(), filter_by()
    # 返回类型是querybase
    stu = Students.query.filter(Students.s_name == '厂长')
    stu = Students.query.filter_by(s_name='莉哥')
    # all(), first()
    stus = Students.query.all()
    stu = Students.query.filter(Students.s_age==19).first()
    # 执行sql
    sql = 'select * from students;'
    stus = db.session.execute(sql)
    # 模糊查询姓名包含王的学生信息
    # select * from students where s_name like '%王%'
    # select * from students where s_name like '王%'
    # select * from students where s_name like '_王%'
    stu = Students.query.filter(Students.s_name.contains('王'))
    stu = Students.query.filter(Students.s_name.startswith('王'))

    # 查询id在某个范围之内的学生信息
    # select * from students where id in (2,3,4,5,6)
    stus = Students.query.filter(Students.id.in_([2,3,4,5,6]))

    # 查询年龄大于19的学生信息
    stus = Students.query.filter(Students.s_age > 19)
    stus = Students.query.filter(Students.s_age.__gt__(19))

    # 查询id=2的学生信息
    # get()获取主键对应的行数据
    stu = Students.query.filter(Students.id == 2).first()
    stu = Students.query.get(2)

    # offset+limit
    stus = Students.query.limit(3)
    stus = Students.query.offset(0).limit(3)

    # order_by()
    # stus = Students.query.order_by('id')
    stus = Students.query.order_by('-id')

    # 查询姓名中包含王的，并且年龄等于23
    stus = Students.query.filter(Students.s_name.contains('王'),
                                 Students.s_age == 23)
    # 查询姓名中包含王，或年龄等于23
    # django中： filter(Q(A) | Q(B))
    # flask中: filter(or_(A, B))
    from sqlalchemy import or_, not_
    stus = Students.query.filter(or_(Students.s_name.contains('王'),
                                 Students.s_age == 23))
    # 查询姓名中不包含王，且年龄等于23
    stus = Students.query.filter(not_(Students.s_name.contains('王')),
                                 Students.s_age == 23)

    return '查询学生'


@blue.route('/delete_stu/<int:id>/')
def delete_stu(id):
    # 删除
    stu = Students.query.filter(Students.id == id).first()
    db.session.delete(stu)
    db.session.commit()
    return '删除成功'


@blue.route('/update_stu/<int:id>/')
def update_stu(id):
    # 修改
    stu = Students.query.filter_by(id=id).first()
    stu.s_name = '哈哈'
    stu.save()
    return '修改成功'


@blue.route('/paginate/', methods=['GET'])
def stu_page():
    page = int(request.args.get('page', 1))
    # 1. offset+limit
    stus = Students.query.offset((page-1) * 2).limit(2)
    # 2. 切片
    stus = Students.query.all()[(page-1)*2:page*2]
    # 3. sql
    sql = 'select * from students limit %s,%s' % ((page-1)*2, 2)
    stus = db.session.execute(sql)
    # 4. paginate()方法
    paginate = Students.query.paginate(page, 2)
    stus = paginate.items
    return render_template('stus.html', stus=stus, paginate=paginate)

# 1. 创建班级信息
# 2. 指定班级和学生的关联关系


@blue.route('/create_grade/')
def create_grade():
    grades_names = ['物联网', '微电子学', '英语', 'LOL']
    for name in grades_names:
        grade = Grade()
        grade.g_name = name
        db.session.add(grade)
        db.session.commit()
    return '创建成功'


@blue.route('/rel_stu_grade/')
def rel_stu_grade():
    stus_ids = [2,3,4]
    for id in stus_ids:
        stu = Students.query.get(id)
        # 在flask中 stu.s_g获取的值为int类型.
        # 在django中 stu.s_g获取的是对象，stu.s_g_id获取到的int类型
        stu.s_g = 1
        stu.save()
    return '关联学生和班级'


@blue.route('/sel_stu_by_grade/')
def sel_stu_by_grade():
    # 通过班级查找学生
    grade = Grade.query.filter(Grade.g_name == '物联网').first()
    # 获取到班级对应的学生信息
    stus = grade.students
    return '通过班级查找学生信息'


@blue.route('/sel_grade_by_stu/')
def sel_grade_by_stu():
    stu = Students.query.get(5)
    # 获取班级， 学生对象.backref
    grade = stu.grade
    return '通过学生获取班级信息'

# 添加课程信息
# 添加课程和学生的关联关系


@blue.route('/add_stu_cou/')
def add_stu_cou():
    stu = Students.query.get(2)
    # 学生的对象查找课程信息，stu.cou
    cou1 = Course.query.get(1)
    cou2 = Course.query.get(2)
    cou3 = Course.query.get(3)
    # 绑定学生和课程的关联关系
    stu.cou.append(cou1)
    stu.cou.append(cou2)
    stu.cou.append(cou3)

    stu.save()
    return '小明选课成功'


