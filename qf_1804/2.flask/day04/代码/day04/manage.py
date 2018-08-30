
from flask import Flask
from flask_script import Manager
from flask_debugtoolbar import DebugToolbarExtension

from app.views import blue
from app.models import db
from utils import api

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/app')

# 数据库配置
# dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

# 绑定sqlalchemy和app
db.init_app(app)

# 设置debug为True
app.debug = True
# 绑定toolbar和app
toolbar = DebugToolbarExtension()
toolbar.init_app(app)

# 绑定api和app
api.init_app(app)

manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()
