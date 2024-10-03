from typing import Final, cast

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import error, success, warning
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


INVALID_PASSWORDS: Final[str] = 'Senhas incompatíveis ou menores de 8 caracteres.'
INVALID_EMAIL: Final[str] = 'Email inválido.'
INVALID_USERNAME: Final[str] = 'Username inválido.'
INVALID_NAMES: Final[str] = 'Nome/sobrenome inválidos.'
USER_CREATED: Final[str] = 'Usuário criado com sucesso. Informe um ADM para ativá-lo.'
INVALID_CREDENTIALS: Final[str] = 'Credenciais inválidas.'
USER_NOT_FOUND: Final[str] = 'Usuário não encontrado.'
USER_INACTIVE: Final[str] = 'Usuário inativo.'


def register_view(req: HttpRequest) -> HttpResponse:
    if req.user.is_authenticated:
        return redirect(reverse('home:index'))

    elif req.method != 'POST':
        return render(req, 'account/register.html')

    email: str | None = req.POST.get('email')
    username: str | None = req.POST.get('username')
    first: str | None = req.POST.get('first')
    last: str | None = req.POST.get('last')
    password: str | None = req.POST.get('password')
    password2: str | None = req.POST.get('password2')

    if not password or not password2 or password != password2 or len(password) < 8:
        error(req, INVALID_PASSWORDS)
        return render(req, 'account/register.html')

    elif User.objects.filter(email=email).exists() or email is None:
        error(req, INVALID_EMAIL)
        return render(req, 'account/register.html')

    elif User.objects.filter(username=username).exists() or username is None:
        error(req, INVALID_USERNAME)
        return render(req, 'account/register.html')

    elif first is None or last is None:
        error(req, INVALID_NAMES)
        return render(req, 'account/register.html')

    user: User = User.objects.create_user(
        username=username,
        email=email,
        first_name=first.strip(),
        last_name=last.strip(),
        password=password,
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

    username: str | None = req.POST.get('username')
    password: str | None = req.POST.get('password')

    if username is None or password is None:
        error(req, INVALID_CREDENTIALS)
        return render(req, 'account/login.html')

    user: User | None = cast(
        User | None, authenticate(username=username.strip(), password=password.strip())
    )

    if user is None:
        error(req, USER_NOT_FOUND)
        return render(req, 'account/login.html')

    elif not user.is_active:
        warning(req, USER_INACTIVE)
        return render(req, 'account/login.html')

    login(req, user)
    return redirect(reverse('home:index'))


@login_required
def logout_view(req: HttpRequest) -> HttpResponse:
    logout(req)
    return redirect(reverse('account:login'))
