from os import environ
from typing import cast

from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application


environ.setdefault('DJANGO_SETTINGS_MODULE', 'CORE.settings.dev')

app = application = cast(WSGIHandler, get_wsgi_application())
