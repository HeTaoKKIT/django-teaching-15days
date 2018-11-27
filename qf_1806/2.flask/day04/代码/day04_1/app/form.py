
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo

from app.models import User


class RegisterForm(FlaskForm):

    username = StringField('用户名', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    password2 = StringField('password2',
                   validators=[DataRequired(),
                              EqualTo('password', '密码不一致')])

    submit = SubmitField('提交')


    def validate_username(self, field):
        # 验证用户是否注册
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('用户已经注册')
        if len(field.data) > 6:
            raise ValidationError('用户名不能超过6个字符')
        if len(field.data) < 3:
            raise ValidationError('用户名不能少于3个字符')
        # 验证密码是否相等


