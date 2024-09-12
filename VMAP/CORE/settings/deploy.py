# ruff: noqa: F403 F405

from os import getenv

import dj_database_url

from CORE.settings.base import *

DATABASES = {"default": dj_database_url.parse(str(getenv("DATABASE_URL")))}

DEBUG: bool = False
SECRET_KEY: str | None = getenv("SECRET_KEY")
ALLOWED_HOSTS: list[str] = str(getenv("ALLOWED_HOSTS")).split(",")


# HTTP -> HTTPS redirect
SECURE_PROXY_SSL_HEADER: tuple[str, str] = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT: bool = True
