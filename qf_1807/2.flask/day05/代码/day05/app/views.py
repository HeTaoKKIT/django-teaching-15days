import os

from flask import Blueprint, request, render_template, \
    jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from app.form import UserRegisterForm
from app.models import User
from utils import status_code
from utils.settings import MEDIA_PATH

blue = Blueprint('user', __name__)


@blue.route('/register/', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            # 保存
            user = User()
            user.username = username
            # from werkzeug.security import generate_password_hash
            password = generate_password_hash(password)
            user.password = password
            user.save()
            return '创建成功'
        else:
            return render_template('register.html', form=form)


@blue.route('/login/', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


@blue.route('/login/', methods=['POST'])
def my_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 校验字段的完整性
        if not all([username, password]):
            return jsonify(status_code.USER_LOGIN_PARAMS_IS_INVALID)
        # 判断用户是否注册
        user = User.query.filter(User.username==username).first()
        if not user:
            return jsonify({'code': 10002, 'msg': '用户没有注册，请去注册'})
        # 校验密码
        if not check_password_hash(user.password, password):
            return jsonify({'code': 10003, 'msg': '密码不正确'})
        session['user_id'] = user.id
        return jsonify({'code': 200, 'msg': '请求成功'})


@blue.route('/index/')
def index():
    user = User.query.filter(User.username == 'coco').first()
    return render_template('index.html', user=user)


@blue.route('/icon/', methods=['GET', 'POST'])
def icon():
    if request.method == 'GET':
        return render_template('icon.html')

    if request.method == 'POST':
        # 1. 获取图片
        icon = request.files.get('icon')
        # 2. 保存图片
        # path: E:/wordspace/7.flask/day05/static/media/xxxx.jpg
        path = os.path.join(MEDIA_PATH, icon.filename)
        icon.save(path)
        # 3. 修改字段
        user = User.query.filter(User.username=='coco').first()
        user.icon = icon.filename
        user.save()
        return redirect(url_for('user.index'))

