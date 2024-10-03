from typing import Final, cast

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import error, success
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


INVALID_PASSWORDS: Final[str] = 'Senhas incompatíveis ou menores de 8 caracteres.'
INVALID_EMAIL: Final[str] = 'Email inválido.'
INVALID_USERNAME: Final[str] = 'Username inválido.'
INVALID_NAMES: Final[str] = 'Nome/sobrenome inválido.'
USER_CREATED: Final[str] = 'Usuário criado com sucesso. Informe um ADM para ativá-lo.'
INVALID_CREDENTIALS: Final[str] = 'Credenciais inválidas.'
USER_INACTIVE: Final[str] = 'Usuário inativo.'


def register_view(req: HttpRequest) -> HttpResponse:
    if req.user.is_authenticated:
        return redirect(reverse('home:index'))

    elif req.method != 'POST':
        return render(req, 'account/register.html')

    first: str | None = req.POST.get('first')
    last: str | None = req.POST.get('last')
    username: str | None = req.POST.get('username')
    email: str | None = req.POST.get('email')
    password: str | None = req.POST.get('password')
    password2: str | None = req.POST.get('password2')

    if not password or not password2 or password != password2 or len(password) < 8:
        error(req, INVALID_PASSWORDS)
        return render(req, 'account/register.html')

    elif User.objects.filter(email=email).exists() or email is None:
        error(req, INVALID_EMAIL)
        return render(req, 'account/register.html')

    elif first is None or last is None:
        error(req, INVALID_NAMES)
        return render(req, 'account/register.html')

    if username is None or User.objects.filter(username=username).exists():
        error(req, INVALID_USERNAME)
        return render(req, 'account/register.html')

    user: User = User.objects.create_user(
        username=username.strip(),
        email=email.strip(),
        first_name=first.strip().title(),
        last_name=last.strip().title(),
        password=password.strip(),
    )
    user.is_active = False
    user.save()

    success(req, USER_CREATED)
    return redirect(reverse('account:login'))


def login_view(req: HttpRequest) -> HttpResponse:
    if req.user.is_authenticated:
        return redirect(reverse('home:index'))

    elif req.method != 'POST':
        return render(req, 'account/login.html')

    raw_username: str | None = req.POST.get('username')
    raw_password: str | None = req.POST.get('password')

    if raw_username is None or raw_password is None or len(raw_password) < 8:
        error(req, INVALID_CREDENTIALS)
        return render(req, 'account/login.html')

    username: str = raw_username.strip()
    password: str = raw_password.strip()

    user: User | None = cast(
        User | None, authenticate(req, username=username, password=password)
    )

    if user is None:
        error(req, INVALID_CREDENTIALS)
        return render(req, 'account/login.html')

    login(req, user)
    return redirect(reverse('home:index'))


@login_required
def logout_view(req: HttpRequest) -> HttpResponse:
    logout(req)
    return redirect(reverse('account:login'))
