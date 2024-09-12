from django.urls import URLPattern, path

from . import views

app_name = "account"

urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]
