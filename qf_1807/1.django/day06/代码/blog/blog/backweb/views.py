from django.shortcuts import render


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
