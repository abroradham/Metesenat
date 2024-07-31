from rest_framework import serializers

from apps.student.models import Student
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone", "full_name"]


class StudentUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['user', 'university',  'tuition_fee']

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = instance.get("user")

        for attr, value in user_data.items():
            setattr(user, attr, value)

        user.save()
        return super().update(instance, validated_data)
