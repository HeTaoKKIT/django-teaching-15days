
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from app.models import OrderModel
from users.models import UserModel, UserTicketModel
from utils.functions import get_ticket


def my(request):
    if request.method == 'GET':
        user = request.user
        data = {}
        if user.id:
            orders = OrderModel.objects.filter(user=user)
            wait_pay, payed = 0, 0
            for order in orders:
                if order.o_status:
                    payed += 1
                else:
                    wait_pay += 1
            data['payed'] = payed
            data['wait_pay'] = wait_pay

        return render(request, 'mine/mine.html', data)


def login(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {}
        # 验证数据是否完整
        if not all([username, password]):
            data['msg'] = '请填写完整的信息'
        if UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.get(username=username)
            if check_password(password, user.password):
                # 存票ticket在cookie中
                ticket = get_ticket()
                res = HttpResponseRedirect(reverse('user:my'))
                out_time = datetime.now() + timedelta(days=1)
                res.set_cookie('ticket', ticket, expires=out_time)
                # 存ticket在userTicket表中
                UserTicketModel.objects.create(user=user,
                                               ticket=ticket,
                                               out_time=out_time)
                return res
            else:
                data['msg'] = '密码错误'
        else:
            data['msg'] = '用户名错误'
        return render(request, 'user/user_login.html', data)


def register(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        icon = request.FILES.get('icon')
        # 如果提交的数据有为空的情况
        if not all([username, email, password]):
            data = {
                'msg': '请填写完整的字段信息'
            }
            return render(request, 'user/user_register.html', data)

        UserModel.objects.create(username=username,
                                 password=make_password(password),
                                 email=email,
                                 icon=icon)

        return HttpResponseRedirect(reverse('user:login'))

