
from flask import Blueprint, render_template, \
    request, session, redirect, url_for

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