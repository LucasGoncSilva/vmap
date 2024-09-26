from typing import cast

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import error, success, warning
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here
def register_view(req: HttpRequest) -> HttpResponse:
    if req.user.is_authenticated:
        return redirect(reverse("home:index"))

    elif req.method != "POST":
        return render(req, "account/register.html")

    email: str | None = req.POST.get("email")
    username: str | None = req.POST.get("username")
    first: str | None = req.POST.get("first")
    last: str | None = req.POST.get("last")
    password: str | None = req.POST.get("password")
    password2: str | None = req.POST.get("password2")

    if not password or not password2 or password != password2 or len(password) < 8:
        error(
            req,
            "Senhas não conferem com o esperado: incompatíveis ou menores de 8 caracteres.",
        )
        return render(req, "account/register.html")

    elif User.objects.filter(email=email).exists() or email is None:
        error(req, "Email inválido.")
        return render(req, "account/register.html")

    elif User.objects.filter(username=username).exists() or username is None:
        error(req, "Username inválido.")
        return render(req, "account/register.html")

    elif first is None or last is None:
        error(req, "Nome/sobrenome inválidos.")
        return render(req, "account/register.html")

    user: User = User.objects.create_user(
        username=username,
        email=email,
        first_name=first.strip(),
        last_name=last.strip(),
        password=password,
    )
    user.is_active = False
    user.save()

    success(req, "Usuário criado com sucesso. Informe um ADM para ativá-lo.")
    return redirect(reverse("account:login"))


def login_view(req: HttpRequest) -> HttpResponse:
    if req.user.is_authenticated:
        return redirect(reverse("home:index"))

    elif req.method != "POST":
        return render(req, "account/login.html")

    username: str | None = req.POST.get("username")
    password: str | None = req.POST.get("password")

    if username is None or password is None:
        error(req, "Credenciais inválidas.")
        return render(req, "account/login.html")

    user: User | None = cast(
        User | None, authenticate(username=username.strip(), password=password.strip())
    )

    if user is None:
        error(req, "Usuário não encontrado.")
        return render(req, "account/login.html")

    elif not user.is_active:
        warning(req, "Usuário inativo.")
        return render(req, "account/login.html")

    login(req, user)
    return redirect(reverse("home:index"))


@login_required
def logout_view(req: HttpRequest) -> HttpResponse:
    if req.method != "POST":
        return redirect(reverse("home:index"))

    logout(req)
    return redirect(reverse("account:login"))
