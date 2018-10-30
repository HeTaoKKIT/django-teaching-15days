from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import UserToken


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 做登录验证
        # func是被login_required装饰的函数
        # 屏蔽掉登录和注册的url，不需要做登录验证
        not_check = ['/user/login/', '/user/register/']
        path = request.path
        if path in not_check:
            # 不继续执行以下登录验证的代码，直接去执行视图函数
            return None

        token = request.COOKIES.get('token')
        if not token:
            # cookie中没有登录的标识符，跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()
        if not user_token:
            # token标识符有误，跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))

        return None

