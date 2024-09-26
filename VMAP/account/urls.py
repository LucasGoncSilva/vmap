from typing import Final

from django.urls import URLPattern, path

from . import views

app_name: Final[str] = "account"

urlpatterns: Final[list[URLPattern]] = [
    path("", views.login_view, name="empty_login"),
    path("login", views.login_view, name="login"),
    path("cadastro", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
]
