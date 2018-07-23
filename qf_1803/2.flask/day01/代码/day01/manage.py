
from flask import Flask
from flask_script import Manager

from app.views import app_blueprint

app = Flask(__name__)
app.register_blueprint(app_blueprint, url_prefix='/app')

manage = Manager(app)

if __name__ == '__main__':
    # app.run(debug=True, host='127.0.0.1', port=8081)
    manage.run()


