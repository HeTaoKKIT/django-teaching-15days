
from flask import Flask
from flask_script import Manager

# 初始化一个Flask对象
from app.views import blueprint

app = Flask(__name__)

# 第二步:注册蓝图
app.register_blueprint(blueprint=blueprint, url_prefix='/app')

# 使用Manager管理Flask的对象
manage = Manager(app=app)

# 启动项目，run()
if __name__ == '__main__':
    # port: 端口，host：IP地址，debug调试模式
    # app.run(port=8080, host='0.0.0.0', debug=True)

    # python manage.py runserver -d -p 8080 -h 0.0.0.0
    manage.run()


