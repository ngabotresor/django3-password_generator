from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    lenght = int(request.GET.get('length', 12))
    characters = list("abcdefjhigklmnopqrstuvwxyz")

    if request.GET.get('Number'):
        characters.extend(list("0123456789"))

    if request.GET.get('UpperCase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get('special'):
        characters.extend(list("!@#$%&^*"))

    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'passwords': thepassword})


def About(request):
    return render(request, 'generator/About.html')
