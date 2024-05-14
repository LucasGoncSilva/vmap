from django.contrib import admin
from django.urls import include, path, URLResolver


urlpatterns: list[URLResolver] = [
    # System's routes
    # Admin's routes
    path('admin/', admin.site.urls),
    # User's routes
    # path('conta/', include('account.urls')),
]
