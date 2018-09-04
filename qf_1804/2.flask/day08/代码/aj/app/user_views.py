
import re
import os
import random

from flask import Blueprint, request, render_template, jsonify, \
    session

from app.models import db, User
from utils import status_code

# 初始化蓝图对象
from utils.functions import is_login
from utils.settings import UPLOAD_DIR

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('create_all/')
def create_all():
    # 创建数据库中的表
    db.create_all()
    return '创建数据库成功'


@user_blueprint.route('register/', methods=['GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')


@user_blueprint.route('img_code/', methods=['GET'])
def img_code():
    # 获取随机长度为4的验证码
    s='1234567890qwertyuiopasdfghjklzxcvbnmm'
    code = ''
    for i in range(4):
        code += random.choice(s)
    # 将状态码code存放在session中
    session['code'] = code
    return jsonify({'code': 200, 'msg': '请求成功', 'data': code})


@user_blueprint.route('register/', methods=['POST'])
def my_register():
    # 实现注册功能
    # 获取注册页面ajax提交过来的参数，request.form
    mobile = request.form.get('mobile')
    imagecode = request.form.get('imagecode')
    passwd = request.form.get('passwd')
    passwd2 = request.form.get('passwd2')
    # 校验参数是否填写完整
    if not all([mobile, imagecode, passwd, passwd2]):
        return jsonify(status_code.USER_REGISTER_PARAMS_NOT_EXISTS)
    # 校验手机号
    if not re.match(r'^1[345678]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_PHONE_IS_NOT_VALID)
    # 校验图片验证码
    if session.get('code') != imagecode:
        return jsonify(status_code.USER_REGISTER_CODE_IS_NOT_VALID)
    # 校验密码是否一致
    if passwd != passwd2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_NOT_EQUAL)
    # 判断手机号是否注册过
    user = User.query.filter(User.phone==mobile).all()
    if user:
        return jsonify(status_code.USER_REGISTER_PHONE_IS_EXISTS)
    # 保存用户的注册信息
    user = User()
    user.phone = mobile
    user.name = mobile
    user.password = passwd
    user.add_update()
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('login/', methods=['GET'])
def login():
    return render_template('login.html')


@user_blueprint.route('my_login/', methods=['GET'])
def my_login():
    # 获取手机号和密码
    mobile = request.args.get('mobile')
    passwd = request.args.get('passwd')
    # 校验参数是否完整
    if not all([mobile, passwd]):
        return jsonify(status_code.USER_LOGIN_PARAMS_NOT_EXISTS)
    # 校验手机号是否符合规格
    if not re.match(r'^1[345678]\d{9}$', mobile):
        return jsonify(status_code.USER_LOGIN_PHONE_IS_NOT_VALID)
    # 判断手机号是否存在
    user = User.query.filter(User.phone == mobile).first()
    if not user:
        return jsonify(status_code.USER_LOGIN_IS_NOT_EXISTS)
    # 校验密码是否正确
    if not user.check_pwd(passwd):
        return jsonify(status_code.USER_LOGIN_PASSWORD_IS_NOT_VALID)
    # 记录用户登录成功
    session['user_id'] = user.id
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('my/', methods=['GET'])
@is_login
def my():
    return render_template('my.html')


@user_blueprint.route('my_info/', methods=['GET'])
@is_login
def my_info():
    user_id = session['user_id']
    user = User.query.get(user_id)
    user_info = user.to_basic_dict()
    return jsonify(user_info=user_info, code=status_code.OK)


@user_blueprint.route('logout/', methods=['GET'])
@is_login
def logout():
    session.clear()
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('profile/', methods=['GET'])
@is_login
def profile():
    return render_template('profile.html')


@user_blueprint.route('profile/', methods=['PATCH'])
@is_login
def my_profile():
    # 获取头像
    avatar = request.files.get('avatar')
    user_id = session['user_id']
    if avatar:
        # 保存用户头像,保存在media
        # 保存图片到/static/media/upload/xxx.jpg
        avatar.save(os.path.join(UPLOAD_DIR, avatar.filename))
        # 修改用户的头像字段
        user = User.query.get(user_id)
        upload_avatar_path = os.path.join('upload', avatar.filename)
        user.avatar = upload_avatar_path

        user.add_update()
        return jsonify(code=status_code.OK, img_avatar=upload_avatar_path)

    else:
        return jsonify(status_code.USER_PROFILE_AVATAR_IS_NOT_EXISTS)


@user_blueprint.route('profile_name/', methods=['PATCH'])
@is_login
def profile_name():
    # 修改用户名
    # 获取用户名，校验用户名是否已经存在
    username = request.form.get('username')
    if not User.query.filter(User.name==username).count():
        # 更新用户名
        user = User.query.get(session['user_id'])
        user.name = username
        user.add_update()
        return jsonify(status_code.SUCCESS)
    else:
        # 如果用户名存在，则返回错误信息
        return jsonify(status_code.USER_PROFILE_NAME_IS_EXISTS)


@user_blueprint.route('auth/', methods=['GET'])
def auth():
    return render_template('auth.html')


@user_blueprint.route('auth/', methods=['PATCH'])
def my_auth():
    # 获取用户名和身份证号
    real_name = request.form.get('real_name')
    id_card = request.form.get('id_card')
    # 校验参数
    if not all([real_name, id_card]):
        return jsonify(status_code.USER_AUTH_PARAMS_IS_NOT_VALID)
    if not re.match(r'^[1-9]\d{16}[1-9X]$', id_card):
        return jsonify(status_code.USER_AUTH_ID_CARD_IS_NOT_VALID)
    # 修改用户的信息
    user = User.query.get(session['user_id'])
    user.id_card = id_card
    user.id_name = real_name
    user.add_update()
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('auth_info/', methods=['GET'])
@is_login
def auth_info():
    user = User.query.get(session['user_id'])
    user_info = user.to_auth_dict()
    return jsonify(user_info=user_info, code=status_code.OK)

