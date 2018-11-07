
from django.utils.deprecation import MiddlewareMixin

from user.models import User


class UserAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # TODO: 判断某些页面需要登录才能访问，某些也许不需要登录就可以访问
        # TODO：需要登录的页面，当用户没有登录时，该如何处理？
        # 给request.user赋值，赋的值为当前登录系统的用户对象
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            request.user = user
        return None
