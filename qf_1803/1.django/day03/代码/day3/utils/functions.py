
import random

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from app.models import MyUser


def is_login(func):
    """
    用于登录的装饰器
    """
    def checkout_login(request):
        ticket = request.COOKIES.get('ticket')
        if ticket:
            user = MyUser.objects.filter(ticket=ticket)
            if user:
                return func(request)
            else:
                return HttpResponseRedirect(reverse('a:my_login'))
        else:
            return HttpResponseRedirect(reverse('a:my_login'))
    return checkout_login


def get_ticket():
    s= '1234567890qwertyuioplkjhgfdsazxcvbnm'
    ticket = ''
    for i in range(25):
        ticket += random.choice(s)
    return ticket

