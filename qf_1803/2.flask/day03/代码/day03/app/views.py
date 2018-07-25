
from datetime import datetime

from flask import Blueprint, redirect, url_for, \
    abort, render_template, request, session

from app.models import db, Student

from utils.functions import is_login

app_blue = Blueprint('first', __name__)


@app_blue.route('/')
def hello():
    return 'hello 美女！'


@app_blue.route('/getRedirect/')
def get_redirect():
    # 第一种跳转，地址固定
    # return redirect('/app/')
    # 使用反向解析，url_for('初始化蓝图的第一个参数.函数名')
    return redirect(url_for('first.hello'))


@app_blue.route('/getError')
def get_error():
    try:
        3/0
    except Exception as e:
        abort(400)

    return '计算'


@app_blue.errorhandler(400)
def handler(exception):
    return '捕获的异常：%s' % exception


@app_blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = session.get('username')
        return render_template('login_p.html', username=username)

    if request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        return redirect(url_for('first.login'))


@app_blue.route('/new_login/', methods=['GET', 'POST'])
def new_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        # 数据库校验，用户密码是否正确
        if username == '妲己' and password == '123123':
            session['user_id'] = 1
            return redirect((url_for('first.index')))
        else:
            return redirect(url_for('first.new_login'))


@app_blue.route('/index/', methods=['GET'])
# @is_login
def index():
    list1 = [1,2,3,4,5,6,7,8]
    p1 = '<h3>今天天气真好！三班女生最美</h3>'
    p2 = '    <h3>今天天气真好，三班女生最美</h3>    '
    return render_template('index.html', list1=list1, p1=p1, p2=p2)


@app_blue.route('/create_db/', methods=['GET'])
def create_db():
    # 创建数据库中的表
    db.create_all()
    return '创建数据表'


@app_blue.route('/drop_db/', methods=['GET'])
def drop_db():
    db.drop_all()
    return '删除数据库'


@app_blue.route('/create_stu/', methods=['POST', 'GET'])
def create_stu():
    if request.method == 'GET':
        return render_template('addstu.html')
    else:
        s_name = request.form.get('s_name')
        s_age = request.form.get('s_age')

        stu = Student()
        stu.s_name = s_name
        stu.s_age = s_age
        stu.s_create_time = datetime.now()

        db.session.add(stu)
        db.session.commit()
        return '创建数据成功'

@app_blue.route('/selstu/', methods=['GET'])
def sel_stu():
    stus = Student.query.all()
    return render_template('stus.html', stus=stus)


@app_blue.route('/detailstu/<int:id>/', methods=['GET'])
def detail_stu(id):

    # filter过滤
    stu = Student.query.filter(Student.id==id)
    # filter_by过滤
    stu = Student.query.filter_by(id=id)
    # get,获取不到数据不报错
    # stu = Student.query.get(id)

    return render_template('stus.html', stus=stu)


@app_blue.route('/update_stu/<int:id>/', methods=['PATCH'])
def update_stu(id):

    s_name = request.form.get('s_name')
    # 第一种修改方式
    # stu = Student.query.get(id)
    # stu.s_name = s_name

    # 第二种
    Student.query.filter_by(id=id).update({'s_name': s_name})
    Student.query.filter(Student.id==id).update({'s_name': s_name})
    # db.session.add(stu)
    db.session.commit()
    return '修改数据成功'


@app_blue.route('/del_stu/<int:id>/', methods=['DELETE'])
def del_stu(id):
    stu = Student.query.get(id)
    # stu.delete()
    db.session.delete(stu)
    db.session.commit()
    return '删除成功'

