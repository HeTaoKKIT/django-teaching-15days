import uuid

from flask import Flask
from flask_script import Manager

from app.views import app_blueprint

app = Flask(__name__)

# 第二步，注册蓝图
app.register_blueprint(blueprint=app_blueprint, url_prefix='/app')


# 使用Manager管理app对象
manage = Manager(app)



if __name__ == '__main__':
    # host主机地址
    # port端口
    # app.run(host='0.0.0.0', port=8080, debug=True)
    manage.run()
    # python manage.py runserver -p -h -d
