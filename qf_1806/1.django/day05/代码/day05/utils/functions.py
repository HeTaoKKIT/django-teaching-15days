
from django.http import HttpResponseRedirect

# 定义登录验证的装饰器
# 闭包三个条件
# 1. 外层函数套内层函数
# 2. 内层函数调用外层函数的参数
# 3. 外层函数返回内层函数
from django.urls import reverse

from user.models import UserToken


def login_required(func):
    def check_login(request):
        # func是被login_required装饰的函数
        token = request.COOKIES.get('token')
        if not token:
            # cookie中没有登录的标识符，跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()
        if not user_token:
            # token标识符有误，跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)
    return check_login
