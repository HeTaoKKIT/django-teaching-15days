
from flask import Flask

from utils.config import Conf
from app.views import blue
from app.models import db
from utils.settings import TEMPLATE_PATH, STATIC_PATH


def create_app():

    app = Flask(__name__,
                static_folder=STATIC_PATH,
                template_folder=TEMPLATE_PATH)
    # 加载配置
    app.config.from_object(Conf)
    # 蓝图
    app.register_blueprint(blueprint=blue, url_prefix='/user')
    # 初始化
    db.init_app(app)

    return app
