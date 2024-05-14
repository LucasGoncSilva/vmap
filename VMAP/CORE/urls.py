from django.contrib import admin
from django.urls import path, URLPattern


urlpatterns: list[URLPattern] = [
    # System's routes
    # Admin's routes
    path('admin/', admin.site.urls),
    # User's routes
]
