
# 1. 外层函数内嵌内层函数
# 2. 外层函数返回内层函数
# 3. 内层函数调用外层函数的参数
from django.http import HttpResponse

from user.models import MyUser


def check_permissions(func):

    def check(request):
        # coco用户有查看用户列表权限，才能访问index函数。使用装饰器去写
        user = MyUser.objects.filter(username='coco').first()
        # 验证权限
        u_p = user.user_permissions.filter(codename='all_my_user').first()
        if u_p:
            # 用户有列表权限，则继续访问被装饰器装饰的函数
            return func(request)
        else:
            return HttpResponse('用户没有查看列表权限，不能访问方法')
    return check
