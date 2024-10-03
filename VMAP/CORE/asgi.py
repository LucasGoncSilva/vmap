from os import environ
from typing import cast

from django.core.asgi import get_asgi_application
from django.core.handlers.wsgi import WSGIHandler


environ.setdefault('DJANGO_SETTINGS_MODULE', 'CORE.settings.dev')

app = application = cast(WSGIHandler, get_asgi_application())
