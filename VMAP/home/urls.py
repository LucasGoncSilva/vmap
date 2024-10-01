from typing import Final

from django.urls import URLPattern, path

from home import views

app_name: Final[str] = "home"

urlpatterns: Final[list[URLPattern]] = [path("", views.index, name="index")]
