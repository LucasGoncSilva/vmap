from typing import Final

from django.urls import URLPattern, path

from . import views

app_name: Final[str] = "account"

urlpatterns: list[URLPattern] = [
    path("", views.login, name="empty_login"),
    path("login", views.login, name="login"),
    path("cadastro", views.register, name="register"),
]
