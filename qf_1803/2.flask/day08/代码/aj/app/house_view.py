
import os

from flask import Blueprint, render_template, session, \
    jsonify, request

from app.models import User, Area, House, HouseImage, Facility
from utils import status_code
from utils.functions import is_login
from utils.settings import upload_folder

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/myhouse/', methods=['GET'])
def myhouse():
    return render_template('myhouse.html')


@house_blueprint.route('/house_info/', methods=['GET'])
@is_login
def house_info():
    user = User.query.get(session['user_id'])
    if user.id_card:
        # 实名认证成功
        houses = House.query.filter(House.user_id==session['user_id']).order_by('-id')
        houses_list = [house.to_dict() for house in houses]
        return jsonify(code=status_code.OK, houses_list=houses_list)
    else:
        return jsonify(status_code.HOUSE_USER_INFO_ID_CARD_INVALID)


@house_blueprint.route('/newhouse/', methods=['GET'])
def newhouse():
    return render_template('newhouse.html')


@house_blueprint.route('/area_facility/', methods=['GET'])
def area_facility():
    areas = Area.query.all()
    facilitys = Facility.query.all()

    areas_json = [area.to_dict() for area in areas]
    facilitys_json = [facility.to_dict() for facility in facilitys ]

    return jsonify(code=status_code.OK, areas=areas_json, facilitys=facilitys_json)


@house_blueprint.route('/newhouse/', methods=['POST'])
@is_login
def my_newhouse():
    # 保存房屋信息，设施信息
    house_dict = request.form

    house = House()
    house.user_id = session['user_id']
    house.price = house_dict.get('price')
    house.title = house_dict.get('title')
    house.area_id = house_dict.get('area_id')
    house.address = house_dict.get('address')
    house.room_count = house_dict.get('room_count')
    house.acreage = house_dict.get('acreage')
    house.unit = house_dict.get('unit')
    house.capacity = house_dict.get('capacity')
    house.beds = house_dict.get('beds')
    house.deposit = house_dict.get('deposit')
    house.min_days = house_dict.get('min_days')
    house.max_days = house_dict.get('max_days')

    facilitys = house_dict.getlist('facility')
    for facility_id in facilitys:
        facility = Facility.query.get(facility_id)
        # 多对多关联
        house.facilities.append(facility)
    house.add_update()

    return jsonify(code=status_code.OK, house_id=house.id)


@house_blueprint.route('/house_images/', methods=['POST'])
def house_images():
    # 创建房屋图片
    house_id = request.form.get('house_id')
    image = request.files.get('house_image')

    # 保存图片  /static/media/upload/xxx.jpg
    save_url = os.path.join(upload_folder, image.filename)
    image.save(save_url)
    # 保存房屋和图片信息
    house_image = HouseImage()
    house_image.house_id = house_id
    image_url = os.path.join('upload', image.filename)
    house_image.url = image_url
    house_image.add_update()
    # 创建房屋首图
    house = House.query.get(house_id)
    if not house.index_image_url:
        house.index_image_url = image_url
        house.add_update()
    return jsonify(code=status_code.OK, image_url=image_url)


@house_blueprint.route('/detail/', methods=['GET'])
def detail():
    return render_template('detail.html')


@house_blueprint.route('/house_detail/<int:id>/', methods=['GET'])
def house_detail(id):
    house = House.query.get(id)
    return jsonify(code=status_code.OK, house=house.to_full_dict())
