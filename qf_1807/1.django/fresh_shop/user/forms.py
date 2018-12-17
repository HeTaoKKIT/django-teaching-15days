
from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=20, min_length=5,
                                required=True, error_messages={
                                'required': '用户名必填',
                                'max_length': '用户名不能超过20位字符',
                                'min_length': '用户名不能少于5位字符'
                            })
    pwd = forms.CharField(max_length=20, min_length=8,
                          required=True,error_messages={
                            'required': '密码必填',
                            'max_length': '密码不能超过20位字符',
                            'min_length': '密码不能短于8位字符'
                        })
    cpwd = forms.CharField(max_length=20, min_length=8,
                          required=True,error_messages={
                            'required': '密码必填',
                            'max_length': '密码不能超过20位字符',
                            'min_length': '密码不能短于8位字符'
                        })
    email = forms.CharField(required=True, error_messages={
                            'required': '邮箱必填'
                        })

    # 验证时，会自动调用
    def clean(self):
        # 校验用户名是否已存在于数据库
        username = self.cleaned_data.get('user_name')
        user = User.objects.filter(username=username).first()
        if user:
            # 用户已存在于数据库，抛出异常
            raise forms.ValidationError({'user_name': '该用于已注册，请去登陆'})
        # 校验密码是否相等
        pwd = self.cleaned_data.get('pwd')
        cpwd = self.cleaned_data.get('cpwd')
        if pwd != cpwd:
            raise forms.ValidationError({'pwd': '两次密码不一致'})

        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=5,
                                required=True, error_messages={
                                'required': '用户名必填',
                                'max_length': '用户名不能超过20位字符',
                                'min_length': '用户名不能少于5位字符'
                            })
    pwd = forms.CharField(max_length=20, min_length=8,
                          required=True,error_messages={
                            'required': '密码必填',
                            'max_length': '密码不能超过20位字符',
                            'min_length': '密码不能短于8位字符'
                        })

    def clean(self):
        # 验证登录的账号是否已经被注册过，注册过才能登录
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError({'username': '账号没有注册，请去注册'})

        return self.cleaned_data


class UserAddressForm(forms.Form):
    signer_name = forms.CharField(required=True, error_messages={'required': '必填'})
    address = forms.CharField(required=True, error_messages={'required': '必填'})
    postcode = forms.CharField(required=True, error_messages={'required': '必填'})
    mobile = forms.CharField(required=True, error_messages={'required': '必填'})
