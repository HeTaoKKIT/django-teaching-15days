
from flask import Blueprint, redirect, url_for, \
    abort, render_template, request, session

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
    return render_template('index.html')