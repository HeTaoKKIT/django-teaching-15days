from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from app.models import Grade, Student, MyUser, Role, Promission
from utils.functions import is_login, get_ticket


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 登录验证
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 验证用户名和密码是否能从数据库中匹配到user对象
        # User.objects.filter(username=username, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            # 验证通过
            auth.login(request, user)
            # return render(request, 'index.html')
            return HttpResponseRedirect(reverse('a:index'))
        else:
            # 验证不通过
            return render(request, 'login.html')


def register(request):
    # 注册
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        # 第一种
        # return HttpResponseRedirect('/app/login/')
        # 第二种
        return HttpResponseRedirect(reverse('a:login'))


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('a:login'))


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

        # ticket = request.COOKIES.get('ticket')
        # if ticket:
        #     user = MyUser.objects.filter(ticket=ticket)
        #     if user:
        #         return render(request, 'index.html')
        #     else:
        #         return HttpResponseRedirect(reverse('a:my_login'))
        # else:
        #     return HttpResponseRedirect(reverse('a:my_login'))


def head(request):
    if request.method == 'GET':
        return render(request, 'head.html')


def left(request):
    if request.method == 'GET':
        return render(request, 'left.html')


def grade(request):
    if request.method == 'GET':
        num = request.GET.get('page_num', 1)
        grades = Grade.objects.all()
        paginator = Paginator(grades, 2)
        page = paginator.page(num)
        return render(request, 'grade.html', {'grades': page})


def addstu(request):
    if request.method == 'GET':
        grades = Grade.objects.all()
        return render(request, 'addstu.html', {'grades': grades})

    if request.method == 'POST':
        s_name = request.POST.get('s_name')
        s_sex = request.POST.get('s_sex')
        g_id = request.POST.get('g')
        img = request.FILES.get('s_img')

        Student.objects.create(s_name=s_name, s_sex=s_sex,
                               g_id=g_id, img=img)
        # g = Grade.objects.filter(id=g_id).first()
        # Student.objects.create(s_name=s_name, s_sex=s_sex, g=g)
        return HttpResponseRedirect(reverse('a:student'))



def student(request):
    if request.method == 'GET':
        stus = Student.objects.all()
        return render(request, 'student.html', {'stus': stus})


def addgrade(request):
    if request.method == 'GET':
        return render(request, 'addgrade.html')

    if request.method == 'POST':
        grade_name = request.POST.get('grade_name')
        Grade.objects.create(g_name=grade_name)
        return HttpResponseRedirect(reverse('a:grade'))


def delstu(request):
    if request.method == 'GET':
        s_id = request.GET.get('s_id')
        Student.objects.filter(id=s_id).delete()
        return HttpResponseRedirect(reverse('a:student'))

def editgrade(request):
    if request.method == 'GET':
        g_id = request.GET.get('g_id')
        g = Grade.objects.filter(id=g_id).first()
        return render(request, 'addgrade.html', {'g': g})

    if request.method == 'POST':
        g_id = request.POST.get('g_id')
        grade_name = request.POST.get('grade_name')
        grade = Grade.objects.get(id=g_id)
        grade.g_name = grade_name
        grade.save()
        return HttpResponseRedirect(reverse('a:grade'))


def my_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        password = make_password(password)
        MyUser.objects.create(username=username, password=password)

        return HttpResponseRedirect(reverse('a:my_login'))

def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 先验证用户是否存在
        if MyUser.objects.filter(username=username).exists():
            user = MyUser.objects.get(username=username)
            if check_password(password, user.password):
                # 在客户端cookie中保存一个ticket值
                res = HttpResponseRedirect(reverse('a:index'))
                ticket = get_ticket()
                res.set_cookie('ticket', ticket)
                # 在服务端存同样的一个ticket值
                user.ticket = ticket
                user.save()
                return res
            else:
                return HttpResponseRedirect(reverse('a:my_login'))
        else:
            return HttpResponseRedirect(reverse('a:my_login'))


def test(request):
    if request.method == 'GET':
        # 查询用户id=1有那些权限
        user = MyUser.objects.get(id=1)
        user_permissions = [i.p_name for i in user.r.r_p.all()]

        # 查询有班级列表权限的用户
        p = Promission.obejects.get(p_name='GRADELIST')
        for i in range(len(p.role_set.all())):
            p.role_set.all()[i].myuser_set.all()


def base(request):
    if request.method == 'GET':
        return render(request, 'base_index.html')



