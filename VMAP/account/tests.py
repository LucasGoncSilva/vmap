from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class BaseViewTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            username="user",
            password="password",
        )

        self.REGISTER_ENDPOINT: str = "account:register"
        self.LOGIN_ENDPOINT: str = "account:login"
        self.ALT_LOGIN_ENDPOINT: str = "account:empty_login"
        self.LOGOUT_ENDPOINT: str = "account:logout"

        self.REGISTER_TEMPLATE: str = "account/register.html"
        self.LOGIN_TEMPLATE: str = "account/login.html"
        self.LOGOUT_TEMPLATE: str = "account/logout.html"
        self.HOME_TEMPLATE: str = "home/index.html"


class RegisterViewTestCase(BaseViewTestCase):
    def test_GET_anonymous_user(self) -> None:
        """GET /conta/ | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.get(reverse(self.REGISTER_ENDPOINT))

        self.assertEqual(res.status_code, 200)

        res: HttpResponse = self.client.get(
            reverse(self.REGISTER_ENDPOINT), follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.REGISTER_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_GET_authenticated_user(self) -> None:
        """GET /conta/ | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.get(reverse(self.REGISTER_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.get(
            reverse(self.REGISTER_ENDPOINT), follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_empty(self) -> None:
        """POST /conta/ | anonymous user | empty form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(reverse(self.REGISTER_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.REGISTER_TEMPLATE)
        # TODO: validar mensagem de erro.
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_empty(self) -> None:
        """POST /conta/ | authenticated user | empty form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.REGISTER_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT), follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_missing_required(self) -> None:
        """POST /conta/ | anonymous user | missing required form data"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        data = {
            "email": "testemail@example.com",
            "first": "First",
            "last": "Last",
            "password": "123oliveira4",
            "password2": "123oliveira4",
        }

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT),
            data=data,
            follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.REGISTER_TEMPLATE)
        # TODO: validar mensagem de erro.
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_missing_required(self) -> None:
        """POST /conta/ | authenticated user | missing required form data"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        data = {
            "email": "testemail@example.com",
            "first": "First",
            "last": "Last",
            "password": "123oliveira4",
            "password2": "123oliveira4",
        }

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT),
            data=data,
            follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_already_existent(self) -> None:
        """POST /conta/ | anonymous user | already existent user data"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        data = {
            "email": "user",
            "email": "testemail@example.com",
            "first": "First",
            "last": "Last",
            "password": "password",
            "password2": "password",
        }

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT),
            data=data,
            follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.REGISTER_TEMPLATE)
        # TODO: validar mensagem de erro.
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_already_existent(self) -> None:
        """POST /conta/ | authenticated user | already existent user data"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        data = {
            "email": "user",
            "email": "testemail@example.com",
            "first": "First",
            "last": "Last",
            "password": "password",
            "password2": "password",
        }

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT),
            data=data,
            follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_valid(self) -> None:
        """POST /conta/ | anonymous user | valid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        data = {
            "email": "testemail@example.com",
            "username": "usernamename",
            "first": "First",
            "last": "Last",
            "password": "123oliveira4",
            "password2": "123oliveira4",
        }

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT),
            data=data,
            follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # TODO: validar mensagem de retorno.
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_valid(self) -> None:
        """POST /conta/ | authenticated user | valid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        data = {
            "email": "testemail@example.com",
            "username": "usernamename",
            "first": "First",
            "last": "Last",
            "password": "123oliveira4",
            "password2": "123oliveira4",
        }

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT),
            data=data,
            follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)


class LoginViewTestCase(BaseViewTestCase):
    def test_GET_anonymous_user(self) -> None:
        """GET /conta/ | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.get(reverse(self.LOGIN_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_GET_authenticated_user(self) -> None:
        """GET /conta/ | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.get(reverse(self.LOGIN_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.get(reverse(self.LOGIN_ENDPOINT), follow=True)

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_invalid(self) -> None:
        """POST /conta/ | anonymous user | invalid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(reverse(self.LOGIN_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # TODO: validar mensagem de erro
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_invalid(self) -> None:
        """POST /conta/ | authenticated user | invalid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.LOGIN_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.post(reverse(self.LOGIN_ENDPOINT), follow=True)

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_valid(self) -> None:
        """POST /conta/ | anonymous user | valid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(
            reverse(self.LOGIN_ENDPOINT),
            data={"username": "user", "password": "password"},
            follow=True,
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Anonymous user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_valid(self) -> None:
        """POST /conta/ | authenticated user | valid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.LOGIN_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.post(reverse(self.LOGIN_ENDPOINT), follow=True)

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_GET_anonymous_user_alt(self) -> None:
        """GET /conta/ | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.get(reverse(self.ALT_LOGIN_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_GET_authenticated_user_alt(self) -> None:
        """GET /conta/ | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.get(reverse(self.ALT_LOGIN_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.get(
            reverse(self.ALT_LOGIN_ENDPOINT), follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_invalid_alt(self) -> None:
        """POST /conta/ | anonymous user | invalid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(reverse(self.ALT_LOGIN_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # TODO: validar mensagem de erro
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_invalid_alt(self) -> None:
        """POST /conta/ | authenticated user | invalid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.ALT_LOGIN_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.post(
            reverse(self.ALT_LOGIN_ENDPOINT), follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_valid_alt(self) -> None:
        """POST /conta/ | anonymous user | valid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(
            reverse(self.ALT_LOGIN_ENDPOINT),
            data={"username": "user", "password": "password"},
            follow=True,
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Anonymous user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_valid_alt(self) -> None:
        """POST /conta/ | authenticated user | valid form"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.ALT_LOGIN_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.post(
            reverse(self.ALT_LOGIN_ENDPOINT), follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)


class LogoutViewTestCase(BaseViewTestCase):
    def test_GET_anonymous_user(self) -> None:
        """GET /conta/logout | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.get(reverse(self.LOGOUT_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.get(reverse(self.LOGOUT_ENDPOINT), follow=True)

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_GET_authenticated_user(self) -> None:
        """GET /conta/logout | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.get(reverse(self.LOGOUT_ENDPOINT), follow=True)

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.HOME_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user(self) -> None:
        """POST /conta/logout | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(reverse(self.LOGOUT_ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.post(reverse(self.LOGOUT_ENDPOINT), follow=True)

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user(self) -> None:
        """POST /conta/logout | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.LOGOUT_ENDPOINT), follow=True)

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Logged user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)
