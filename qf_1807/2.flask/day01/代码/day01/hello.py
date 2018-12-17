
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

# 路由:'/stu/<id>/', http:127.0.0.1:5000/stu/10/

@app.route('/stu/<id>/')
def stu(id):
    # 接收的id参数为字符串
    return 'stu id: %s' % id

@app.route('/grade/<int:id>/')
def grade(id):
    # 接收的id参数为整型
    return 'grade id: %d' % id


@app.route('/name/<string:name>/')
def name(name):
    # 接收为字符串的name参数
    # <string:name>等同于<name>
    return 'name: %s' % name


@app.route('/float/<float:price>/')
def get_price(price):
    # 接收为浮点类型的price参数
    return 'price: %s' % price


@app.route('/path/<path:url>/')
def get_path(url):
    # 接收URL中path后面的全部路径
    return 'url: %s' % url


@app.route('/get_uuid/')
def get_uuid():
    import uuid
    return str(uuid.uuid4())


@app.route('/uuid/<uuid:u>/')
def my_uuid(u):
    # 接收参数u为uuid类型的值
    return 'uuid: %s' % u


if __name__ == '__main__':
    manage = Manager(app)
    # python hello.py runserver -h 0.0.0.0 -p 8080 -d
    manage.run()
    # app.run(host='0.0.0.0', port=8080, debug=True)

# 127.0.0.1:5000/hello
