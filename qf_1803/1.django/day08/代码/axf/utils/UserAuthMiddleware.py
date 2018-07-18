
import re
from datetime import datetime

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from users.models import UserTicketModel


class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 验证用户的登录状态
        paths = ['/user/login/', '/user/register/',
                 '/axf/market/', '/axf/marketparams/(\d+)/(\d+)/(\d+)/']
        # if request.path in paths:
        #     return None

        for path in paths:
            if re.match(path, request.path):
                return None

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect(reverse('user:login'))

        user = UserTicketModel.objects.filter(ticket=ticket).first()
        if not user:
            return HttpResponseRedirect(reverse('user:login'))

        if user.out_time.replace(tzinfo=None) < datetime.now():
            user.delete()
            return HttpResponseRedirect(reverse('user:login'))

        request.user = user.user
