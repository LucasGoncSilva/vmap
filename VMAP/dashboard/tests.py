from typing import Final

from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class DashboardViewTestCase(TestCase):
    ENDPOINT: Final[str] = "dashboard:index"
    TEMPLATE: Final[str] = "dashboard/index.html"

    def setUp(self) -> None:
        User.objects.create_user(
            username="user",
            password="password",
        )

    def test_GET_anonymous_user(self) -> None:
        """GET /dashboard | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.get(reverse(self.ENDPOINT))

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.get(reverse(self.ENDPOINT), follow=True)

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateNotUsed(res, self.TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_GET_authenticated_user(self) -> None:
        """GET /dashboard | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.get(reverse(self.ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_POST_anonymous_user(self) -> None:
        """POST /dashboard | anonymous user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        res: HttpResponse = self.client.post(reverse(self.ENDPOINT), {"DATA": "HERE"})

        self.assertEqual(res.status_code, 302)

        res: HttpResponse = self.client.post(
            reverse(self.ENDPOINT), {"DATA": "HERE"}, follow=True
        )

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateNotUsed(res, self.TEMPLATE)
        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

    def test_POST_authenticated_user(self) -> None:
        """POST /dashboard | authenticated user"""

        # Anonymous user check
        self.assertTrue(get_user(self.client).is_anonymous)
        self.assertFalse(get_user(self.client).is_authenticated)

        self.assertTrue(self.client.login(username="user", password="password"))

        res: HttpResponse = self.client.post(reverse(self.ENDPOINT))

        # Success response check
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, self.TEMPLATE)
        # Logged user check
        self.assertFalse(get_user(self.client).is_anonymous)
        self.assertTrue(get_user(self.client).is_authenticated)
