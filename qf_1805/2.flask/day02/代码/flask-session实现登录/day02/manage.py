import redis
from flask import Flask
from flask_script import Manager
from flask_session import Session

from user.views import user_blueprint

app = Flask(__name__)
app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

# session配置
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

# 获取Session对象，并初始化app
se = Session()
se.init_app(app)

manage = Manager(app=app)


if __name__ == '__main__':
    manage.run()
