from django.shortcuts import render

from home.models import MainWheel, MainNav, MainMustBuy,\
    MainShop, MainShow


def index(request):
    if request.method == 'GET':

        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainmustbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()

        data = {
            'mainwheels':  mainwheels,
            'mainnavs': mainnavs,
            'mainmustbuys': mainmustbuys,
            'mainshops': mainshops,
            'mainshows': mainshows
        }
        return render(request, 'home/home.html', data)
