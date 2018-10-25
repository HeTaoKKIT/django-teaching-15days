from django.shortcuts import render

from app.models import Student

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def all_stu(request):
    if request.method == 'GET':
        # 获取所有学生的信息
        stus = Student.objects.all()
        content_h2 = '<h2>今天天气真好</h2>'
        return render(request, 'stus.html', {'stus': stus, 'content_h2': content_h2})

