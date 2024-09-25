from typing import Final

from django.urls import URLPattern, path

from . import views

app_name: Final[str] = "about"

urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]
