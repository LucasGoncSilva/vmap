from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
@login_required
def index(req: HttpRequest) -> HttpResponse:
    return render(req, "dashboard/index.html")
