
from datetime import datetime

from flask import Blueprint, render_template, request, url_for, \
    session, jsonify

from app.models import Order, House
from utils import status_code
from utils.functions import is_login

order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('order/', methods=['POST'])
@is_login
def order():
    # 创建订单模型
    # 1. 获取开始和结束的时间
    begin_date = datetime.strptime(request.form.get('begin_date'), '%Y-%m-%d')
    end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')

    # 2. 获取当前用户和房屋id
    user_id = session['user_id']
    house_id = request.form.get('house_id')
    # 获取房屋对象
    house = House.query.get(house_id)

    order = Order()
    order.user_id = user_id
    order.house_id = house_id
    order.begin_date = begin_date
    order.end_date = end_date
    order.days = (end_date - begin_date).days + 1
    order.amount = order.days * house.price
    order.house_price = house.price
    order.add_update()
    return jsonify(status_code.SUCCESS)


@order_blueprint.route('orders/', methods=['GET'])
def orders():
    return render_template('orders.html')


@order_blueprint.route('orders_info/', methods=['GET'])
@is_login
def orders_info():
    orders = Order.query.filter(Order.user_id==session['user_id'])
    orders_info = [order.to_dict() for order in orders]
    return jsonify(code=status_code.OK, orders_info=orders_info)


@order_blueprint.route('lorders/', methods=['GET'])
def lorders():
    return render_template('lorders.html')


@order_blueprint.route('lorder_info/', methods=['GET'])
@is_login
def lorder_info():
    # 获取别人对自己的房屋进行下单的信息
    # 先查询自己发布的房屋信息
    houses = House.query.filter(House.user_id == session['user_id'])
    house_ids = [house.id for house in houses]
    # 查询订单
    orders = Order.query.filter(Order.house_id.in_(house_ids))
    lorder_info = [order.to_dict() for order in orders]
    return jsonify(code=status_code.OK, lorder_info=lorder_info)
