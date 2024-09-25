from django.urls import URLPattern, path

from . import views

app_name = "home"

urlpatterns: list[URLPattern] = [
    path("", views.index, name="home"),
]
