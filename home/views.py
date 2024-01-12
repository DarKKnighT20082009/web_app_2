from django.http import HttpResponse
from django.shortcuts import render

from home.models import Vazifa, User


def home_page(request):
    vazifalar = Vazifa.objects.all()

    context = {
        "vazifalar": vazifalar
    }
    return render(request, template_name='templates/bosh_sahifa.html', context=context)


def odamlar(request):
    users = User.objects.all()

    context = {
        "users": users
    }
    return render(request, template_name="templates/odamlar_sahifa.html", context=context)
