from rest_framework import serializers

from apps.sponsor.models import Sponsor, SponsorType
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['full_name', 'phone']


class SponsorDetailUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sponsor
        fields = ("id", "user", "amount", "created_at", "status", "type", "company")
        extra_kwargs = {"id": {"read_only": True}}


    def validate(self, data):
        if data.get("type") == SponsorType.INDIVIDUAL and not data.get("company"):
            raise serializers.ValidationError(
                {
                    "company" : "This field is required for individual sponsors"
                }
            )
        return data
    

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)

        user.save()
        return super().update(instance, validated_data)

