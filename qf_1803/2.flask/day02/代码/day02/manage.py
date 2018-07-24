
from flask import Flask
from flask_script import Manager
from flask_session import Session

import redis

from app.views import app_blue

app = Flask(__name__)
app.register_blueprint(app_blue, url_prefix='/app')

# session的配置
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# 第一种
se = Session()
se.init_app(app)
# 第二种
# Session(app=app)


manager = Manager(app)

if __name__ == '__main__':
    manager.run()

