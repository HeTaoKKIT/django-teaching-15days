from django.shortcuts import render


def my(request):
    if request.method == 'GET':
        return render(request, 'mine/mine.html')


def login(request):
    if request.method == 'GET':

        # cookie中存验证的ticket值

        # 服务端UserTicket中存用户和ticket的关联关系
        return render(request, 'user/user_login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')
