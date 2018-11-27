
from flask import Blueprint, render_template, request, url_for, jsonify
from sqlalchemy import and_, not_, or_
from werkzeug.utils import redirect

from app.models import db, Student, Grade, Course

blue = Blueprint('app', __name__)


@blue.route('/')
def hello():
    1/0
    return 'hello'


@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建数据库成功'


@blue.route('/add_stu/', methods=['POST'])
def add_stu():
    # 插入数据
    stu = Student()
    stu.s_name = '小张'
    # db.session.add(stu)
    # db.session.commit()
    stu.save()
    return '创建学生成功'


@blue.route('/del_stu/', methods=['DELETE'])
def del_stu():
    # 删除数据
    stu = Student.query.filter(Student.s_name == '小明').first()
    db.session.delete(stu)
    db.session.commit()
    return '删除学生成功'


@blue.route('/up_stu/', methods=['PATCH'])
def up_stu():
    # 第一种方式
    # stu = Student.query.filter(Student.s_name == '小张').first()
    # stu.s_name = '小傻子'
    # stu.save()
    # 第二种，使用update
    Student.query.filter(Student.s_name == '小傻子').update({'s_name': '小张'})
    db.session.commit()

    return '更新学生成功'


@blue.route('/sel_stu/', methods=['GET'])
def sel_stu():
    # filter(模型名.字段 == ‘值’)
    # filter_by(字段 = ‘值’)
    stu = Student.query.filter_by(s_name='小张').first()
    # all(): 查询所有结果，返回结果的列表
    # first(): 返回对象
    # 注意: 不要写all().first()

    # 查询id为2的学生，使用get()方法
    stu = Student.query.filter(Student.id == 2).first()
    # get(): 获取主键所在行的对象。如果获取不到，返回空。
    stu = Student.query.get(2)

    # order_by(): 排序
    # 降序: -id、id desc
    # 升序: id、id asc
    stu = Student.query.order_by('-id')

    # 使用运算符
    # Django的ORM中: filter(s_name__contains='111')
    # Flask的SQLALchemy中: filter(模型名.s_name.contains(''))

    # 例子: 模糊查询姓名中包含'小'的学生信息, contains
    stus = Student.query.filter(Student.s_name.contains('小')).all()

    # startswith, endswith, like _和%, contains
    stus = Student.query.filter(Student.s_name.startswith('小')).all()
    stus = Student.query.filter(Student.s_name.endswith('四')).all()

    # 查询姓名中包含‘李’的学生信息，使用like，_和%
    stus = Student.query.filter(Student.s_name.like('%李%')).all()
    stus = Student.query.filter(Student.s_name.like('_李%')).all()
    stus = Student.query.filter(Student.s_name.like('李%')).all()
    stus = Student.query.filter(Student.s_name.like('%李')).all()

    # in_(): 查询某个范围之内的对象
    stus = Student.query.filter(Student.id.in_([1,2,3,4,5])).all()

    # 查询id大于5的学生信息，__gt__
    # 大于 __gt__，大于等于 __ge__
    # 小于 __lt__，小于等于 __le__
    stus = Student.query.filter(Student.id.__gt__(5)).all()
    stus = Student.query.filter(Student.id > 5).all()

    # 分页
    page = request.args.get('page', 1)
    paginate = Student.query.paginate(int(page), 3)
    stus = paginate.items
    # return render_template('stus.html', stus=stus, paginate=paginate)

    # 例子, 查询性别为男的，且姓名中包含‘小’的学生信息
    # stus = Student.query.filter(Student.gender == 1).filter(Student.s_name.contains('小')).all()
    stus = Student.query.filter(Student.gender == 1,
                                Student.s_name.contains('小')
                                ).all()
    # and_且, not_非, or_或
    stus = Student.query.filter(and_(Student.gender == 1,
                                     Student.s_name.contains('小'))
                                ).all()
    # 例子: 查询性别为男的，或名中包含‘小’的学生信息
    stus = Student.query.filter(or_(Student.gender == 1,
                                    Student.s_name.contains('小'))
                                ).all()
    # 例子: 查询性别不为男，且名中包含‘小’的学生信息
    stus = Student.query.filter(not_(Student.gender == 1),
                                Student.s_name.contains('小')
                                ).all()


    stus_names = [stu.s_name for stu in stus]

    return str(stus_names)

# 添加班级信息
# 学生指定班级


@blue.route('/add_grade/', methods=['POST'])
def add_grade():
    grades = ['一年级', '二年级', '三年级', '四年级']
    g_list = []
    for i in grades:
        g = Grade()
        g.g_name = i
        g_list.append(g)
        # db.session.add(g)
    db.session.add_all(g_list)
    db.session.commit()
    return '创建班级'

# 作业:
# 正向查询: 通过学生查找班级
# 反向查询: 通过班级查询学生


@blue.route('/sel_grade_by_stu/', methods=['GET'])
def sel_grade_by_stu():
    # 通过学生查询班级
    stu = Student.query.filter(Student.s_name=='小张').first()
    # 学生对象.backref
    grade = stu.g
    return '获取班级成功'


@blue.route('/sel_stu_by_grade/', methods=['GET'])
def sel_stu_by_grade():
    grade = Grade.query.get(1)
    stus = grade.student
    return '获取学生成功'


@blue.route('/add_course/', methods=['POST'])
def add_cou():
    cou = Course()
    cou.c_name = '大学物理'
    db.session.add(cou)
    db.session.commit()
    return '创建班级成功'


@blue.route('/all_stu/', methods=['GET'])
def all_stu():
    stus = Student.query.all()
    return render_template('students.html', stus=stus)


@blue.route('/cous/<int:id>/', methods=['GET', 'POST'])
def cous(id):
    if request.method == 'GET':
        cous = Course.query.all()
        return render_template('cous.html', cous=cous)

    if request.method == 'POST':
        # 向中间表s_c中加入数据
        cou_id = request.form.get('cou_id')
        s_id = id
        # 获取对象
        stu = Student.query.get(s_id)
        cou = Course.query.get(cou_id)
        # 关系指定
        stu.cou.append(cou)
        # cou.student.append(stu)
        db.session.commit()
        return redirect(url_for('app.all_stu'))


@blue.route('/del_stu_cou/<int:id>/', methods=['GET', 'DELETE'])
def del_stu_cou(id):
    if request.method == 'GET':
        stu = Student.query.get(id)
        cous = stu.cou
        return render_template('s_c.html', cous=cous, s_id=id)

    if request.method == 'DELETE':
        c_id = request.form.get('c_id')
        s_id = request.form.get('s_id')
        # 获取对象
        stu = Student.query.get(s_id)
        cou = Course.query.get(c_id)
        # 删除学生和课程的关联关系
        stu.cou.remove(cou)
        db.session.commit()
        return jsonify({'code': 200, 'msg': '请求成功'})

# django中中间件:
# process_request
# process_view
# process_templates_response
# process_exception
# process_response

# 钩子函数
# G

@blue.before_request
def before_request():
    print('before_request')


@blue.before_request
def before1_request():
    print('before1_request')


@blue.after_request
def after_request(response):
    print('after_request')
    return response


@blue.teardown_request
def teardown_request(exception):
    print('terardown_request')






