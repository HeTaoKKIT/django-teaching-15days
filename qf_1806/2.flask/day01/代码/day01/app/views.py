import uuid

from flask import Blueprint, redirect, url_for, \
    request, make_response, abort

# 第一步，生成蓝图对象，使用蓝图对象管理理由
app_blueprint = Blueprint('app', __name__)

# request请求
# 获取get传参: request.args
# 获取post传参：request.form
# 获取上传文件: request.files
# 获取路径: request.path
# 请求方式: request.method


@app_blueprint.route('/hello/', methods=['GET', 'POST', 'PATCH'])
def hello():
    # 1/0
    if request.method == 'GET':
        # 获取get提交请求传递的参数: request.args
        # request.args[key] 或request.args.get(key)或request.args.getlist(key)
        return '你好, 双十一'
    if request.method == 'POST':
        # TODO: 获取post提交的参数
        # 获取post提交请求传递的参数: request.form
        return '你好，我是post请求'


# 路由匹配规则
# <选择器:参数名>
# 选择器有int: 表示接受的参数为int类型
# 没有定义选择器: 表示接受的参数为string类型（默认）
# 选择器string: 表示接受的参数一定为string类型
# 选择器 uuid/path/float


@app_blueprint.route('/student/<int:id>/')
def student(id):
    return '我是学号为%d的学生' % id


@app_blueprint.route('/course/<id>/')
def course(id):
    return '我是id为%s的课程' % id


@app_blueprint.route('/hello/<string:name>/')
def hello_name(name):
    return '你好: %s' % name


@app_blueprint.route('/float/<float:number>/')
def hello_float(number):
    return '我是float类型的参数: %s' % number


@app_blueprint.route('/path/<path:name>/')
def path_name(name):
    return 'path: %s' % name


@app_blueprint.route('/get_uuid/')
def get_uuid():
    uu = uuid.uuid4()
    return str(uu)


@app_blueprint.route('/uuid/<uuid:name>/')
def uuid_name(name):
    return 'uuid: %s' % name


@app_blueprint.route('/redirect/')
def redirect_url():
    # Django写法: HttpResponseRedirect(reverse('namespace:name'))
    # Flask写法: redirect(url_for('蓝图名称.跳转的函数名', key=value))
    return redirect(url_for('app.student', id=10))


# 响应response，是后端产生返回给前端（浏览器）
# make_response(响应内容，响应状态码（默认为200）)
# 响应绑定cookie，set_cookie/delete_cookie


@app_blueprint.route('/make_response/', methods=['GET'])
def make_my_reponse():
    res = make_response('<h2>今天天气真好</h2>', 200)
    return res
    # return '<h2>今天天气真好</h2>'


@app_blueprint.route('/abort_a/', methods=['POST'])
def abort_a():
    try:
        a = request.form.get('a')
        b = request.form.get('b')
        c = int(a)/int(b)
        return '%s/%s=%s' % (a, b, c)
    except Exception as e:
        # 异常抛出
        abort(500)


@app_blueprint.errorhandler(500)
def error_handler(error):
    # TODO：返回错误页面
    return 'Exception is %s' % error


