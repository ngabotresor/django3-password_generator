<<<<<<< HEAD
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
=======
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    lenght = int(request.GET.get('lenght', 12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
>>>>>>> 0c5333805cabecea7ff6e9932cf2628ccb127648
