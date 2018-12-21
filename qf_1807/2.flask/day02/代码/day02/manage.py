import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from app.models import db
from app.views import blue

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/app')

app.secret_key = '1212'
# 配置session
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# 配置数据库
# dialect+driver://username:password@host:port/database
# mysql+pymysql://root:123456@127.0.0.1:3306/flask7
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化session和app对象
se = Session()
se.init_app(app)

# 初始化db和app对象
db.init_app(app)


manage = Manager(app)


if __name__ == '__main__':
    manage.run()
