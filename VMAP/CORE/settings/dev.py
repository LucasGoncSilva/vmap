from os import getenv

from dotenv import load_dotenv

from CORE.settings.base import *


load_dotenv()

# docker run --name psql_vmap -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres
DATABASES: dict[str, dict[str, str | Path | None]] = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('DATABASE_NAME', 'postgres'),
        'USER': getenv('DATABASE_USER', 'postgres'),
        'PASSWORD': getenv('DATABASE_PASSWORD', 'postgres'),
        'HOST': getenv('DATABASE_HOST', 'localhost'),
        'PORT': '5432',
    }
}

DEBUG: bool = bool(getenv('DEBUG', DEBUG))
SECRET_KEY: str = getenv('SECRET_KEY', SECRET_KEY)
