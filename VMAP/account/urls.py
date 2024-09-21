from django.urls import URLPattern, path

from . import views


app_name = "account"

urlpatterns: list[URLPattern] = [
    path("", views.login, name="empty_login"),
    path("login", views.login, name="login"),
]
