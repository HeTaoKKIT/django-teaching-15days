
from flask import Flask
from flask_script import Manager

from user.models import db
from user.views import user_blueprint, login_manager

app = Flask(__name__)

app.register_blueprint(blueprint=user_blueprint,
                       url_prefix='/user')

# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/f_login_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

# 没有登录跳转地址
login_manager.login_view = 'user.login'

# 绑定
db.init_app(app)
login_manager.init_app(app)

manage = Manager(app)

if __name__ == '__main__':
    manage.run()
