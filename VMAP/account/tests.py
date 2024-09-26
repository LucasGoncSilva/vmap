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
            email="user@email.com",
        )

        self.REGISTER_ENDPOINT: str = "account:register"
        self.REGISTER_TEMPLATE: str = "account/register.html"
        self.LOGIN_ENDPOINT: str = "account:login"
        self.ALT_LOGIN_ENDPOINT: str = "account:empty_login"
        self.LOGIN_TEMPLATE: str = "account/login.html"


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

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.REGISTER_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user(self) -> None:
        """POST /conta/ | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT), {"DATA": "HERE"}
        )

        self.assertEqual(res.status_code, 200)

        res: HttpResponse = self.client.post(
            reverse(self.REGISTER_ENDPOINT), {"DATA": "HERE"}, follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.REGISTER_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user(self) -> None:
        """POST /conta/ | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.REGISTER_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.REGISTER_TEMPLATE)
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

        self.assertEqual(res.status_code, 200)

        res: HttpResponse = self.client.get(reverse(self.LOGIN_ENDPOINT), follow=True)

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

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user(self) -> None:
        """POST /conta/ | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(
            reverse(self.LOGIN_ENDPOINT), {"DATA": "HERE"}
        )

        self.assertEqual(res.status_code, 200)

        res: HttpResponse = self.client.post(
            reverse(self.LOGIN_ENDPOINT), {"DATA": "HERE"}, follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user(self) -> None:
        """POST /conta/ | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.LOGIN_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_GET_anonymous_user_alt(self) -> None:
        """GET /conta | anonymous user | empty endpoint"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.get(reverse(self.ALT_LOGIN_ENDPOINT))

        self.assertEqual(res.status_code, 200)

        res: HttpResponse = self.client.get(
            reverse(self.ALT_LOGIN_ENDPOINT), follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_GET_authenticated_user_alt(self) -> None:
        """GET /conta | authenticated user | empty endpoint"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.get(reverse(self.ALT_LOGIN_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user_alt(self) -> None:
        """POST /conta | anonymous user | empty endpoint"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(
            reverse(self.ALT_LOGIN_ENDPOINT), {"DATA": "HERE"}
        )

        self.assertEqual(res.status_code, 200)

        res: HttpResponse = self.client.post(
            reverse(self.ALT_LOGIN_ENDPOINT), {"DATA": "HERE"}, follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user_alt(self) -> None:
        """POST /conta | authenticated user | empty endpoint"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.ALT_LOGIN_ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.LOGIN_TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)
