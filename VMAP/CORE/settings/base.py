from pathlib import Path
from typing import Final

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: str = "django-insecure-^%u8*@f-fu=$o$1#oyfrd7%z8&(-3j!ste0&mr-2q2il%t)!9q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = True

ALLOWED_HOSTS: list[str] = ["*"]


# Application definition

INSTALLED_APPS: Final[list[str]] = [
    # Default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd Party
    "whitenoise",
    # Local
    "account",
]

MIDDLEWARE: Final[list[str]] = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "CORE.urls"

TEMPLATES: Final[list[dict[str, str | bool | list | dict | Path]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: Final[str] = "CORE.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES: dict[str, dict[str, str | Path]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: Final[list[dict[str, str]]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE: Final[str] = "pt-br"

TIME_ZONE: Final[str] = "America/Sao_Paulo"

USE_I18N: Final[bool] = True

USE_TZ: Final[bool] = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL: Final[str] = "/static/"
STATIC_ROOT: Final[Path] = BASE_DIR / "staticfiles"
STATICFILES_DIRS: Final[list[Path]] = [
    BASE_DIR / "static",
]
STATICFILES_STORAGE: Final[str] = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD: Final[str] = "django.db.models.BigAutoField"

"""
# User Model
AUTH_USER_MODEL: str = 'account.User'
LOGOUT_REDIRECT_URL: str = 'conta/entrar'


# E-mail configs
EMAIL_BACKEND: str = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST: str = 'smtp.gmail.com'
EMAIL_PORT: int = 587
EMAIL_USE_TLS: bool = True
EMAIL_HOST_USER: str = str(environ.get('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD: str = str(environ.get('EMAIL_HOST_PASSWORD'))
"""


from django.contrib.messages import constants as messages

# Messages configs
MESSAGE_TAGS: dict[int, str] = {
    messages.DEBUG: "alert-primary",
    messages.ERROR: "alert-danger",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
}
