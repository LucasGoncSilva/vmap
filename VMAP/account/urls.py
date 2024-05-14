from django.urls import path, URLPattern

from . import views


app_name = 'account'

urlpatterns: list[URLPattern] = [
    path('', views.index, name='index'),
]
