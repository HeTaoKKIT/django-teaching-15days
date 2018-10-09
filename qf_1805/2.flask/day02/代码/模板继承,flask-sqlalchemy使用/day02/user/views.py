
from flask import Blueprint, render_template, \
    request, session, redirect, url_for

from user.models import db, User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 校验用户名和密码，不能为空
        if not all([username, password]):
            return render_template('login.html')
        if username == 'coco' and password == '123123':
            session['login_status'] = 1
            return redirect(url_for('user.index'))
        else:
            return render_template('login.html')


@user_blueprint.route('/index/', methods=['GET'])
def index():
    return render_template('index.html')


@user_blueprint.route('/scores/', methods=['GET'])
def scores():

    # render(rquest, 'xxx.html', {k1:v1, k2:v2})
    stu_scores = [80,56,31,89,76,34]
    content_h2 = '<h2>hello python</h2>'
    return render_template('scores.html',
                           stu_scores=stu_scores,
                           content_h2=content_h2)


@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建表成功'


@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            return render_template('register.html')
        # 保存注册信息
        user = User()
        user.username = username
        # 密码加密
        user.password = password
        # 保存
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.login'))


