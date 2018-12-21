
from flask import Blueprint, render_template, request, \
    session, url_for, redirect

from app.models import db

blue = Blueprint('app', __name__)


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'coco' and password == '123123':
            session['user_id'] = 1
            return redirect(url_for('app.index'))


@blue.route('/index/')
def index():
    return render_template('index.html')


@blue.route('/temp/')
def temp():
    content = [65,13,76,14,90,64]
    content_h2 = '<h2>今天你们很帅气</h2>'
    content_h2_new = '   <h2>今天你们很帅气</h2>   '
    nums = 10
    return render_template('temp.html', c=content,
                           content_h2=content_h2,
                           content_h2_new=content_h2_new,
                           nums=nums)


@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建数据库成功'


@blue.route('/drop_db/')
def drop_db():
    db.drop_all()
    return '删除数据库成功'
