from typing import Final

from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field: Final[str] = "django.db.models.BigAutoField"
    name: Final[str] = "account"
