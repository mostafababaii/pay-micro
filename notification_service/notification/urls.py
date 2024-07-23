from __future__ import annotations

from django.urls import path
from notification.views import OTPApiView


urlpatterns = [
    path('otp/', OTPApiView.as_view()),
]
