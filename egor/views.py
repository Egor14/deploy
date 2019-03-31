from django.shortcuts import render
from .models import Player


def home_page(request):
    return render(request, 'egor/home_page.html')


def info(request, id):
    obj = Player.objects.get(id=id)
    print(obj)
    return render(request, 'egor/player_info.html', {'obj': obj})