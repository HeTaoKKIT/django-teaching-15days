
from flask import Flask
from flask_script import Manager
from flask_session import Session

import redis

from app.views import blue

app = Flask(__name__)
app.register_blueprint(blueprint=blue, url_prefix='/app')

#  配置session
# 指定redis作为缓存数据库
app.config['SESSION_TYPE'] = 'redis'
# 指定访问哪一个redis，ip和端口
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# 加载app
# 第一种方式
se = Session()
se.init_app(app=app)
# 第二种
# Session(app=app)

manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()
