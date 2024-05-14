from os import getenv

from CORE.settings.base import *


# docker run --name psql_swarden -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres
DATABASES: dict[str, dict[str, str | None]] = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('DATABASE_NAME', 'postgres'),
        'USER': getenv('DATABASE_USER', 'postgres'),
        'PASSWORD': getenv('DATABASE_PASSWORD', 'postgres'),
        'HOST': getenv('DATABASE_HOST', 'localhost'),
        'PORT': '5432',
    }
}

DEBUG = bool(getenv('DEBUG', DEBUG))
SECRET_KEY = getenv('SECRET_KEY', SECRET_KEY)
ALLOWED_HOSTS = list(str(getenv('ALLOWED_HOSTS', ALLOWED_HOSTS)))
CAPTCHA_TEST_MODE = bool(getenv('CAPTCHA_TEST_MODE', False))
