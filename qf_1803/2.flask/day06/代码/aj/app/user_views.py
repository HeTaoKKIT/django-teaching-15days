
import random
import re

from flask import Blueprint, render_template, jsonify,\
    session, request

from app.models import db, User
from utils import status_code

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')


@user_blueprint.route('/create_db/', methods=['GET'])
def create_db():
    db.create_all()
    return '创建数据库成功'


@user_blueprint.route('/get_code/', methods=['GET'])
def get_code():
    code = ''
    s='1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(4):
        code += random.choice(s)
    session['code'] = code
    return jsonify(code=200, msg='请求成功', data=code)


@user_blueprint.route('/register/', methods=['POST'])
def my_register():
    mobile = request.form.get('mobile')
    imagecode = request.form.get('imagecode')
    passwd = request.form.get('passwd')
    passwd2 = request.form.get('passwd2')

    # 验证参数是否完整
    if not all([mobile, imagecode, passwd, passwd2]):
        return jsonify(status_code.USER_REGISTER_PARAMS_VALID)
    # 验证图片验证码是否正确
    if session.get('code') != imagecode:
        return jsonify(status_code.USER_REGISTER_CODE_ERROR)
    # 验证手机号，^1[3456789]\d{9}$
    if not re.match(r'^1[3456789]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_INVALID)
    # 验证密码
    if passwd != passwd2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_ERROR)
    # 验证手机号是否存在
    if User.query.filter(User.phone==mobile).count():
        # 数据库中已存在
        return jsonify(status_code.USER_REGISTER_MOBILE_EXSIST)
    # 数据库中不存在该手机号
    user = User()
    user.phone = mobile
    user.password = passwd
    user.name = mobile
    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@user_blueprint.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@user_blueprint.route('/login/', methods=['POST'])
def my_login():
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    # 校验完整参数
    if not all([mobile, password]):
        return jsonify(status_code.USER_LOGIN_PARAMS_VALID)
    # 验证手机号，^1[3456789]\d{9}$
    if not re.match(r'^1[3456789]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_INVALID)

    user = User.query.filter(User.phone == mobile).first()
    # 校验用户，查看用户是否存在
    if user:
        if user.check_pwd(password):
            # 密码校验成功
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.USER_LOGIN_PASSWORD_INVALID)
    else:
        return jsonify(status_code.USER_LOGIN_PHONE_INVALID)


@user_blueprint.route('/my/', methods=['GET'])
def my():
    return render_template('my.html')
