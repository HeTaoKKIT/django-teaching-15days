
from flask import Blueprint, redirect, url_for, \
    make_response, request, render_template, session

# 模块化管理路由 Blueprint
# 第一步: 生成蓝图对象
blueprint = Blueprint('first', __name__)


@blueprint.route('/')
def hello():
    return 'hello'


@blueprint.route('/stu/<id>/')
def stu(id):
    return 'hello stu: %s' % id


# 1. 定义路由跳转到hello方法
# 2. 定义路由跳转到stu方法

@blueprint.route('/redirect/')
def my_redirect():
    # redirect: 跳转
    # url_for: 反向解析
    # 'first.hello': 蓝图第一个参数.跳转到的函数名
    return redirect(url_for('first.hello'))


@blueprint.route('/redirect_id/')
def stu_redirect():
    return redirect(url_for('first.stu', id=3))


@blueprint.route('/make_response/')
def my_response():
    # make_response创建响应
    # 第一个参数: 响应内容
    # 第二个参数: 响应状态码
    res = make_response('<h2>今天天气很不错</h2>', 200)
    # 设置cookie，max_age以秒为单位，expires以datetime为单位
    res.set_cookie('token', '123456', max_age=6000)
    return res


@blueprint.route('/del_cookie/')
def del_cookie():
    res = make_response('<h2>删除cookie</h2>')
    res.delete_cookie('token')
    return res


@blueprint.route('/req/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def req():
    if request.method == 'GET':
        # 获取GET请求中传递的参数，request.args
        # 获取GET请求中name=小明&name=小花中的name参数，request.args.getlist('name')
        return 'hello get'

    if request.method == 'POST':
        # 获取POST请求中传递的参数，request.form
        # 获取值: request.form.get(key)或request.form.getlist(key)
        return 'hello post'


@blueprint.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        # 模拟登陆
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'coco' and password == '123123':
            session['user_id'] = 1
        return redirect(url_for('first.hello'))

# 作业:
# 1. 登录校验装饰器
