from django.urls import URLPattern, path

from . import views

app_name = "about"

urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]
