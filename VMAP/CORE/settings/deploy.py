from CORE.settings.base import *

from os import getenv


DATABASES: dict[str, dict[str, str | None]] = {
    # 'default': URL
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv.get('DATABASE_NAME'),
        'USER': getenv.get('DATABASE_USER'),
        'PASSWORD': getenv.get('DATABASE_PASSWORD'),
        'HOST': getenv.get('DATABASE_HOST'),
        'PORT': '5432',
    }
}

DEBUG: bool = False
SECRET_KEY: str | None = getenv.get('SECRET_KEY')
ALLOWED_HOSTS: list[str] = str(getenv.get('ALLOWED_HOSTS')).split(',')


# http -> https redirect
SECURE_PROXY_SSL_HEADER: tuple[str, str] = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT: bool = True
