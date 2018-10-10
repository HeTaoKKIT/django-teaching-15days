
from flask import Blueprint


from app.models import db, Students

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