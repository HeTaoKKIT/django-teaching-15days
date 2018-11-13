
from flask import Blueprint, request, render_template, session, \
    redirect, url_for

from app.models import db
from utils.functions import login_required

blue = Blueprint('user', __name__)

# 访问地址:127.0.0.1:8080/app/
@blue.route('/')
def hello():
    return 'hello world'


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # 获取参数
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'coco' and password == '123123':
            # 模拟校验用户名和密码成功，则向session中存储登录成功后的用户id值
            session['user_id'] = 1
            # return redirect(url_for('user.index'))
            return redirect('/app/index/')
        else:
            return render_template('login.html')


@blue.route('/index/')
@login_required
def index():
    user_id = session['user_id']
    return '我是首页, 我的用户id为%s' % user_id


@blue.route('/temp/')
def temp():
    content = ['Python', 'Flask', 'Django', 'Tornado', 'Sanic', 'Twisted']
    content_h2 = '<h2>我是h2标题</h2>'
    content_h22 = '     <h2>我是h2标题</h2>    '
    return render_template('temp.html',
                           title='模板语法',
                           content=content,
                           content_h2=content_h2,
                           content_h22=content_h22)


@blue.route('/create_db/')
def create_db():
    # 第一次迁移模型
    db.create_all()
    return '创建模型成功'


@blue.route('/drop_db/')
def drop_db():
    db.drop_all()
    return '删除模型成功'
