import os

from flask_login import LoginManager, current_user,login_user, logout_user, login_required
from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from user.forms import UserRegiterForm
from user.models import db, User
from utils.settings import UPLOAD_DIR

user_blueprint = Blueprint('user', __name__)

login_manager = LoginManager()


@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    # 表单对象
    form = UserRegiterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        # 验证提交的字段信息
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            # 实现注册，保存用户信息到User模型中
            user = User()
            user.username = username
            user.password = generate_password_hash(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            # 验证失败，form.errors中存在错误信息
            return render_template('register.html', form=form)


@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 校验用户名和密码是否填写完整
        if not all([username, password]):
            return render_template('login.html')
        user = User.query.filter(User.username == username).first()
        if user:
            # 获取到用户，进行密码判断
            if check_password_hash(user.password, password):
                # 密码正确
                # 实现登录， django中auth.login(request, user)
                login_user(user)
                return redirect(url_for('user.index'))
            else:
                error = '密码错误'
                return render_template('login.html', error=error)
        else:
            # 获取不到用户，返回错误信息给页面
            error = '该用户没有注册，请去注册'
            return render_template('login.html', error=error)


@user_blueprint.route('/index/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # 获取图片
        icons = request.files.get('icons')
        # 保存save(path)
        # 作业：
        # 1. 只保存jpg, png....
        # 2. 中间件, 钩子
        # @user_blueprint.before_request
        # @user_blueprint.after_request
        # @user_blueprint.teardown_request
        file_path = os.path.join(UPLOAD_DIR, icons.filename)
        icons.save(file_path)
        # 保存user对象
        user = current_user
        user.icons = os.path.join('upload', icons.filename)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.index'))


@user_blueprint.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.register'))

