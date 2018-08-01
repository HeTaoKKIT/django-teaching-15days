
from flask_script import Manager

from utils.app import create_app

app = create_app()

manage = Manager(app)

if __name__ == '__main__':

    # app.run(debug=True, port=8000, host='127.0.0.1')
    manage.run()