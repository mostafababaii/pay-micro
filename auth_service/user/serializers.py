from __future__ import annotations

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

user = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        lower_email = value.lower()
        # Using Redis Bloom for high-scale applications
        # is a best practice to reduce database connections.
        if user.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError('Duplicate email address')
        return lower_email

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)

        instance.is_active = True
        instance.set_password(password)

        instance.save()
        return instance

    class Meta:
        model = user
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'email': {'required': True},
        }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
