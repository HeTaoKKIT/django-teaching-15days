
from flask import Flask
from flask_script import Manager

from app.views import blueprint

app = Flask(__name__)
# 第二步: 注册蓝图
app.register_blueprint(blueprint=blueprint, url_prefix='/app')

# 加密
app.secret_key = '1asdasdasddfg1212'

manage = Manager(app)
if __name__ == '__main__':
    manage.run()
