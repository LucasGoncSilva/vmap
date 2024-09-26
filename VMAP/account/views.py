from typing import Final

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here
app_name: Final[str] = "account"


def register(req: HttpRequest) -> HttpResponse:
    return render(req, "account/register.html")


def login(req: HttpRequest) -> HttpResponse:
    return render(req, "account/login.html")
