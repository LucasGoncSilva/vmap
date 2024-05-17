from os import getenv

from CORE.settings.base import *


DATABASES: dict[str, dict[str, str | Path | None]] = {
    # 'default': URL
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('DATABASE_NAME'),
        'USER': getenv('DATABASE_USER'),
        'PASSWORD': getenv('DATABASE_PASSWORD'),
        'HOST': getenv('DATABASE_HOST'),
        'PORT': '5432',
    }
}

DEBUG: bool = False
SECRET_KEY: str | None = getenv('SECRET_KEY')
ALLOWED_HOSTS: list[str] = str(getenv('ALLOWED_HOSTS')).split(',')


# HTTP -> HTTPS redirect
SECURE_PROXY_SSL_HEADER: tuple[str, str] = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT: bool = True
