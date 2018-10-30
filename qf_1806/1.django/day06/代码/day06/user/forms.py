
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符',
                                   'min_length': '不能少于2字符'
                               })
    password = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符'
                               })
    password2 = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符'
                               })

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if user:
            raise forms.ValidationError({'username': '账号已注册，请去登陆'})
        pasword = self.cleaned_data.get('password')
        pasword2 = self.cleaned_data.get('password2')
        if pasword != pasword2:
            raise forms.ValidationError({'password': '密码不一致'})
        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符',
                                   'min_length': '不能少于2字符'
                               })
    password = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '不能超过10字符'
                               })

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username':'该账号没有注册，请去注册'})

        return self.cleaned_data

