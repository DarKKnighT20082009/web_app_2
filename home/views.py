
from django.http import HttpResponse

from home.models import Vazifa


def home_page(request):
    return HttpResponse("Hello World! Komron")