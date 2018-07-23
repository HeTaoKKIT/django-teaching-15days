import uuid

from flask import Blueprint, request, make_response

app_blueprint = Blueprint('first', __name__)


@app_blueprint.route('/', methods=['GET', 'POST'])
def hello():

    return "Hello World!"


@app_blueprint.route('/hello', methods=['GET'])
def hello_u():
    return "Hello %s" % '小明'


@app_blueprint.route('/postName', methods=['GET', 'POST', 'PUT'])
def post_name():
    return '我是post请求'


@app_blueprint.route('/GetName/<string:name>', methods=['GET', 'POST', 'PUT'])
def get_name(name):
    return '我是:%s' % name


@app_blueprint.route('/get_id/<int:id>')
def get_id(id):
    print(type(id))
    return '我的年龄：%d' % id


@app_blueprint.route('/get_float/<float:fid>')
def get_fid(fid):
    return '浮点数：%.1f' % fid


@app_blueprint.route('/get_path/<path:path>')
def get_path(path):
    return '路径：%s' % path


@app_blueprint.route('/get_uuid')
def get_uuid():
    uid = uuid.uuid4()
    return 'uid: %s' % uid


@app_blueprint.route('/get_uu/<uuid:uid>')
def get_uu(uid):
    return 'uid: %s' % uid


@app_blueprint.route('/get_response')
def get_response():

    res = make_response('<h2>我是响应</h2>', 202)

    return res
