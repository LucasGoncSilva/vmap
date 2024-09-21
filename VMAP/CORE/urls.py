from django.contrib import admin
from django.urls import URLResolver, include, path

urlpatterns: list[URLResolver] = [
    # System's routes
    # Admin's routes
    path("admin/", admin.site.urls),
    # User's routes
    path("", include("home.urls")),
    path("conta/", include("account.urls")),
]
