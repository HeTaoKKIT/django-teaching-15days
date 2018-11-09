
import random

from user.models import TokenUser


def get_cookie_token():
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    token = ''
    for i in range(20):
        token += random.choice(s)
    return token


# 定义登录验证的装饰器

# 1. 外层函数内嵌内层函数
# 2. 外层函数返回内层函数
# 3. 内层函数调用外层函数的参数

from django.http import HttpResponseRedirect

def is_login(func):

    def check_status(request):
        token = request.COOKIES.get('token')
        if token:
            token_user = TokenUser.objects.filter(token=token).first()
            if token_user:
                # 返回func(request)表示继续执行被is_login装饰的函数
                return func(request)
            else:
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    return check_status



