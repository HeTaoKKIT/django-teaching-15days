from django.shortcuts import render

from app.models import Student


def index(request):
    if request.method == 'GET':
        stus = Student.objects.all()
        return render(request, 'index.html', {'stus': stus})
