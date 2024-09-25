from typing import Final

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
app_name: Final[str] = "home"


@login_required
def index(req: HttpRequest) -> HttpResponse:
    return render(req, "home/index.html")
