
from flask import Blueprint, render_template, session, jsonify

from app.models import User, Area, House, HouseImage, Facility
from utils import status_code
from utils.functions import is_login

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
        # TODO：返回用户的房屋信息
        return jsonify(code=status_code.OK)
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

