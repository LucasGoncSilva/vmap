from os import environ as env

from django.contrib.admin import site as adm_site
from django.urls import URLResolver, include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns: list[URLResolver] = [
    # System's routes
    # Admin's routes
    path("admin/", adm_site.urls),
    # User's routes
    path("", include("home.urls")),
    path("conta/", include("account.urls")),
    path("sobre", include("about.urls")),
    path("dashboard", include("dashboard.urls")),
]

if env.get('DJANGO_SETTINGS_MODULE') == "CORE.settings.dev":
    urlpatterns += debug_toolbar_urls()
