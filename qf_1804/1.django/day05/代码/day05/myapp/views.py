from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    if request.method == 'GET':
        username = request.session.get('username')
        # username = request.session['username']
        print(username)
        # 获取session_key
        session_key = request.session.session_key
        print(session_key)
        # 删除session整条记录
        request.session.delete(session_key)
        # 删除session中的数据
        del request.session['username']
        username = request.session.get('username')
        print(username)
        return render(request, 'index.html')


def setCookie(request):
    if request.method == 'GET':
        res = HttpResponseRedirect(reverse('myapp:index'))
        # 设置cookie值
        # set_cookie(key, value, max_age, expires)
        # 删除：delete_cookie(key)  set_cookie(key, value, max_age=0)
        # res.set_cookie('session_id', '12t861ihafiagdfi', max_age=3)
        # res.delete_cookie('session_id')
        # 设置cookie中的值，并且设置session中的值
        # 登录的时候，进行验证用户的用户名和密码是否正确，如果正确
        request.session['login'] = True
        request.session['username'] = '张三'
        request.session['password'] = '123456'
        return res
