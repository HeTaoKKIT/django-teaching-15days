
from flask import Flask
from flask_script import Manager

from app.views import blue
from app.models import db

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/app')

# 数据库配置
# dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 绑定sqlalchemy和app
db.init_app(app)

manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()
