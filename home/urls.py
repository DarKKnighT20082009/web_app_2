from django.urls import path

from home.views import home_page, odamlar

urlpatterns = [
    path('', home_page, name="blog_list"),
    path('people/', odamlar, name="blog_list")
]
