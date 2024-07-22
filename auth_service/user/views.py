from __future__ import annotations

from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
