
from flask import Flask
from flask_script import Manager

from app.views import blue
from app.models import db

app = Flask(__name__)

app.register_blueprint(blueprint=blue, url_prefix='/app')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False

db.init_app(app)

manage = Manager(app)

if __name__ == '__main__':
    manage.run()
