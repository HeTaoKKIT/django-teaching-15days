
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField

from wtforms.validators import DataRequired, EqualTo, ValidationError

from user.models import User


class UserRegiterForm(FlaskForm):
    # 定义用户名和密码都是必填项
    username = StringField('账号', validators=[DataRequired()])
    password = StringField('密码', validators=[DataRequired()])
    password2 = StringField('确认密码',
                            validators=[DataRequired(), EqualTo('password', '密码不一致')])
    submit = SubmitField('提交')

    def validate_username(self, field):
        user = User.query.filter(User.username == field.data).first()
        if user:
            raise ValidationError('该账号已注册，请去登陆！')

        if len(field.data) < 3:
            raise ValidationError('注册用户名不能少于3个字符')