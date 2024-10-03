from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


@login_required
def index(req: HttpRequest) -> HttpResponse:
    return render(req, 'home/index.html')
