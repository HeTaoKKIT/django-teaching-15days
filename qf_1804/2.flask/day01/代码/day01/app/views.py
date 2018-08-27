
import uuid

from flask import Blueprint, redirect, url_for, request, \
    make_response, abort

# 第一步：初始化蓝图，定义两个参数
blueprint = Blueprint('first', __name__)

# 定义路由，绑定视图函数
@blueprint.route('/')
def hello():
    return 'Hello World'


@blueprint.route('redirect/')
def index():
    # 蓝图第一个参数.视图名
    return redirect(url_for('first.hello'))

# route匹配规则
# 1. <string：xxx>  获取到xxx的参数的值为字符串类型
# 2. <xxx> 默认获取到的xxx的参数的值为字符串类型
# 3. <int:xxx>  获取到的xxx的参数的值为整型类型
# 4. <float:xxx> 获取到xxx为float类型
# 5. <path:xxx> 获取到的xxx为路径后面全部的url地址
# 6. <uuid:xxx>  获取到的xxx值为10038714-fb27-45cd-8a94-eb8dcc4bd44b格式


@blueprint.route('name/<string:s_name>/')
def get_name(s_name):
    return '姓名：%s' % s_name


@blueprint.route('age/<age>/')
def get_age(age):
    return '年龄：%s' % age


@blueprint.route('int_age/<int:age>/')
def get_int_age(age):
    return '年龄：%d'% age


@blueprint.route('float/<float:number>/')
def get_float_number(number):
    return '获取浮点数为：%.2f' % number


@blueprint.route('path/<path:s_path>')
def get_path(s_path):
    return '获取path路径: %s' % s_path


@blueprint.route('get_uuid/')
def get_uuid():
    a = uuid.uuid4()
    return 'uuid:%s' % str(a)


@blueprint.route('uuid/<uuid:s_uuid>/')
def get_by_uuid(s_uuid):
    return '获取uuid值：%s' % s_uuid

# 请求与响应
# 请求：是客户端传到服务端的
# 响应：是服务端返回给客户端的，比如设置cookie值


@blueprint.route('request/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def get_request():
    # 如果是GET请求: 获取get请求中的参数，使用request.args
    # 如果是POST/PUT/PATCH/DELETE请求: 获取请求中的参数，使用request.form
    # 获取key重复的Value值，使用request.form.getlist(key)
    request
    return '我是请求'


@blueprint.route('response/', methods=['GET'])
def get_response():
    # make_response: 创建响应，返给页面
    res = make_response('<h2>我是响应</h2>', 200)

    return 'hello 大美女',200


@blueprint.route('error/', methods=['GET'])
def error():
    a = 9
    b = 0
    try:
        c = a/b
    except:
        abort(500)
    return '%s/%s=%s' % (a,b,c)


@blueprint.errorhandler(500)
def handler_500(exception):
    return '捕捉的异常信息：%s' % exception


@blueprint.route('cookies/', methods=['GET'])
def get_cookies():
    response = make_response('<h3>Hello World</h3>', 200)
    # set_cookie中参数，key，value， max_age/expires
    response.set_cookie('session_id', '1234567890', max_age=1000)
    return response


@blueprint.route('del_cookies/', methods=['GET'])
def del_cookies():
    response = make_response('<h3>Hello World</h3>', 200)
    # 第一种：delete_cookie删除cookie中的key
    # response.delete_cookie('session_id')
    # 第二种：set_cookie，max_age为0，expires=0
    response.set_cookie('session_id', '', max_age=0)
    return response
