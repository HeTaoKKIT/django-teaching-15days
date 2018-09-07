
from flask import url_for, redirect
from flask_script import Manager

from utils.app import create_app

# 创建app
app = create_app()

# 启动首页地址
@app.route('/')
def home_index():
	return redirect(url_for('house.index'))

# 使用Manager管理app
manage = Manager(app=app)

if __name__ == '__main__':
    # 启动run()
    manage.run()

