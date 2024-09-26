from os import environ

from django.core.asgi import get_asgi_application

environ.setdefault("DJANGO_SETTINGS_MODULE", "CORE.settings.dev")

app = application = get_asgi_application()
