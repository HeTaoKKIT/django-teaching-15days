
import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from app.house_views import house_blueprint
from app.models import db

# 初始化Flask对象
from app.order_views import order_blueprint
from app.user_views import user_blueprint

app = Flask(__name__)
# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/aj4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 配置session
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
# 注册蓝图
app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')
app.register_blueprint(blueprint=order_blueprint, url_prefix='/order')

# 绑定app和db
db.init_app(app)
# 绑定session和app
sess = Session()
sess.init_app(app)
# 使用Manager管理app
manage = Manager(app=app)

if __name__ == '__main__':
    # 启动run()
    manage.run()

