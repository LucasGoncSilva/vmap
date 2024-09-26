from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(req: HttpRequest) -> HttpResponse:
    return render(req, "about/index.html")