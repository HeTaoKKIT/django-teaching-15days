
from flask import Blueprint, render_template, request, session, \
    redirect, url_for

blue = Blueprint('app', __name__)


@blue.route('/')
def hello():
    return 'hello'


@blue.route('cart/', methods=['GET', 'POST'])
def cart():
    if request.method == 'GET':
        goods_name = session.get('goods_name')
        return render_template('index.html', goods_name=goods_name)

    if request.method == 'POST':
        # 拿到需要存到redis中的商品的id值
        goods_id = request.form.get('goods_id')
        # 设置值
        session['goods_id'] = goods_id
        session['goods_name'] = 'MAC'
        session['login'] = False
        # 删除
        session.pop('goods_id')
        # 清空所有值
        session.clear()

        return redirect(url_for('app.cart'))


@blue.route('login/', methods=['GET'])
def login():
    goods = [[1,'草莓', 10, 2000], [2, '西瓜', 2, 1000], [3, '李子', 3, 1000]]
    scores = [10, 20, 56, 43, 56, 87, 98, 100]
    content_h2 = '<h2>今天你们又长胖了</h2>'
    content_h3 = '    <h2>今天你们又长胖了</h2>    '
    return render_template('login.html',
                           goods=goods,
                           scores=scores,
                           content_h2=content_h2,
                           content_h3=content_h3)



