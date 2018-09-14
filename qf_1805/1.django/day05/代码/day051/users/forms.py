"""
导入规则：
1. 新引入python自带的库

2. 引入第三方

3. 引入自定义的
"""


from django import forms
from django.contrib.auth.models import User



class UserForm(forms.Form):
    """
    校验注册信息
    """
    username = forms.CharField(required=True, max_length=5, min_length=2,
                               error_messages={
                                   'required': '用户名必填',
                                   'max_length': '用户名不能超过5个字符',
                                   'min_length': '用户名不能少于2个字符'
                               })
    password = forms.CharField(required=True, min_length=6,
                               error_messages={
                                   'required': '密码必填',
                                   'min_length': '密码不能少于6个字符'
                               })
    password2 = forms.CharField(required=True, min_length=6,
                                error_messages={
                                    'required': '确认密码必填',
                                    'min_length': '确认密码不能少于6个字符'
                                })

    def clean(self):
        # 校验用户名是否已经注册过

        user = User.objects.filter(username=self.cleaned_data.get('username'))
        if user:
            # 如果已经注册过
            raise forms.ValidationError({'username': '用户名已存在，请直接登录'})
        # 校验密码和确认密码是否相同
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError({'password': '两次密码不一致'})
        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=5, min_length=2,
                               error_messages={
                                   'required': '用户名必填',
                                   'max_length': '用户名不能超过5个字符',
                                   'min_length': '用户名不能少于2个字符'
                               })
    password = forms.CharField(required=True, min_length=6,
                               error_messages={
                                   'required': '密码必填',
                                   'min_length': '密码不能少于6个字符'
                               })

    def clean(self):
        # 校验用户名是否注册
        user = User.objects.filter(username=self.cleaned_data['username'])
        if not user:
            raise forms.ValidationError({'username': '请先注册再来登录'})
        return self.cleaned_data