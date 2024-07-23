from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.test import TestCase

from .views import UserApiView


class UserApiViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = UserApiView.as_view()

    def test_user_creation(self):
        data = {
            'username': 'testuser',
            'password': 'testpass',
            'email': 'test@example.com',
        }

        request = self.factory.post('/api/users/', data)
        response = self.view(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(get_user_model().objects.count(), 1)

        user = get_user_model().objects.get()

        self.assertEqual(user.username, data['username'])
        self.assertTrue(user.check_password(data['password']))
        self.assertEqual(user.email, data['email'])
