from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.test import TestCase
from rest_framework_simplejwt.tokens import AccessToken

from .views import OTPApiView


class OTPApiViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = OTPApiView.as_view()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass',
            email='test@example.com',
        )
        self.token = AccessToken.for_user(self.user)

    def test_otp_creation(self):
        request = self.factory.post(
            '/api/otp/', {}, HTTP_AUTHORIZATION='Bearer ' + str(self.token),
        )
        response = self.view(request)
        self.assertEqual(response.status_code, 202)
