
from datetime import datetime

from flask import Blueprint, render_template, request, \
    session, jsonify

from app.models import Order, House

from utils import status_code

order_blueprint = Blueprint('order', __name__)


@order_blueprint.route('/booking/', methods=['GET'])
def booking():
    return render_template('booking.html')


@order_blueprint.route('/order/', methods=['POST'])
def order():
    # house_id  start_time end_time
    order_dict = request.form
    house_id = order_dict.get('house_id')
    begin_date = datetime.strptime(order_dict.get('begin_date'), '%Y-%m-%d')
    end_date = datetime.strptime(order_dict.get('end_date'), '%Y-%m-%d')

    house = House.query.get(house_id)

    order = Order()
    order.user_id = session['user_id']
    order.house_id = house_id
    order.begin_date = begin_date
    order.end_date = end_date
    order.days = (end_date - begin_date).days + 1
    order.house_price = house.price
    order.amount = order.days * order.house_price

    order.add_update()

    return jsonify(status_code.SUCCESS)


@order_blueprint.route('/orders/', methods=['GET'])
def orders():
    return render_template('orders.html')


@order_blueprint.route('/my_orders/', methods=['GET'])
def my_orders():
    orders = Order.query.filter(Order.user_id==session['user_id'])
    orders_list = [order.to_dict() for order in orders]
    return jsonify(code=status_code.OK, orders_list=orders_list)


@order_blueprint.route('/lorders/', methods=['GET'])
def lorders():
    return render_template('lorders.html')


@order_blueprint.route('/my_lorders/', methods=['GET'])
def my_lorders():
    user_id = session['user_id']
    houses = House.query.filter(House.user_id==user_id)
    houses_ids = [house.id for house in houses]

    orders = Order.query.filter(Order.house_id.in_(houses_ids))
    orders_list = [order.to_dict() for order in orders]
    return jsonify(code=status_code.OK, orders_list=orders_list)


@order_blueprint.route('/order/', methods=['PATCH'])
def order_status():
    order_id = request.form.get('order_id')
    status = request.form.get('status')
    comment = request.form.get('comment')

    order = Order.query.get(order_id)
    order.status = status
    if comment:
        order.comment = comment
    order.add_update()

    return jsonify(status_code.SUCCESS)

