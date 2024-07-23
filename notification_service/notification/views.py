from __future__ import annotations

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .tasks import send_otp


class OTPApiView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        user = request.user
        send_otp.delay(user.id)
        return Response(status=status.HTTP_202_ACCEPTED)
