from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import authenticate

from apps.users.models import User


class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        phone = data.get('phone')
        password = data.get('password')
        user = authenticate(phone=phone, password=password)
        if user is None or not user.is_superuser:
            raise serializers.ValidationError(
                { "Error" : "Invalid credentials or user is not a superuser."}
                )
        return {
            'user' : user
        }