
from flask import Flask
from flask_script import Manager

from app.models import db
from app.views import user_blueprint

app = Flask(__name__)

app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

app.secret_key = 'asdasdfdg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


manage = Manager(app)


if __name__ == '__main__':
    manage.run()

