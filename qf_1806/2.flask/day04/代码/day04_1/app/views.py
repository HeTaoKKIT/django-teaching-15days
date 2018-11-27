
from flask import redirect, url_for, request, render_template, Blueprint

from werkzeug.security import generate_password_hash, check_password_hash

from app.form import RegisterForm
from app.models import User, db

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            # 验证通过
            # 验证用户是否注册，验证密码和确认密码是否一致
            user = User()
            user.username = form.username.data
            user.password = generate_password_hash(form.password.data)
            db.session.add(user)
            db.session.commit()
            return '注册成功'
        else:
            return redirect(url_for('user.register'))


