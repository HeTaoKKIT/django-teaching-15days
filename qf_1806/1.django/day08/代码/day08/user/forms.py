
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={
                                   'required': '必填'
                               })
    password = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '必填'
                               })