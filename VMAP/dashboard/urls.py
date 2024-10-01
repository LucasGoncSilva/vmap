from typing import Final

from django.urls import URLPattern, path

from dashboard import views

app_name: Final[str] = "dashboard"

urlpatterns: Final[list[URLPattern]] = [path("", views.index, name="index")]
