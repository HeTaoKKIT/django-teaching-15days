
import re

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from users.models import UserTicketModel


class UserMiddelware(MiddlewareMixin):

    def process_request(self, request):

        # 过滤不需要验证的url
        not_check_path = ['/user/login/', '/user/register/',
                          '/home/index/', '/home/market/',
                          '/home/market_params/(\d+)/(\d+)/(\d+)/']

        path = request.path
        # if path in not_check_path:
        #     return None
        for check_path in not_check_path:
            if re.match(check_path, path):
                return None


        ticket = request.COOKIES.get('ticket')
        # 验证ticket是否存在
        if not ticket:
            if path == '/user/mine/':
                return None
            return HttpResponseRedirect(reverse('user:login'))


        # 验证ticket是否能找到用户
        user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
        if not user_ticket:
            if path == '/user/mine/':
                return None
            return HttpResponseRedirect(reverse('user:login'))

        # 删除user_ticket表中的多余数据
        user = user_ticket.user
        UserTicketModel.objects.exclude(user=user, ticket=ticket).delete()

        # 验证成功，向request中的user赋值为当前登录系统的用户
        request.user = user
        # return None 可写可不写
        return None
