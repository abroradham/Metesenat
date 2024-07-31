from rest_framework import serializers


from apps import sponsor
from apps.users.models import User
from apps.sponsor.models import Sponsor, SponsorType


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['full_name', 'phone']

class SponsorCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sponsor
        fields = ['user', 'type', 'company', 'amount']

    def validate(self, data):
        if data.get("type") == SponsorType.INDIVIDUAL and not data.get("company"):
            raise serializers.ValidationError(
                {
                    "company" : "This field is required for individual sponsors"
                }
            )
        return data
    

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)

        return Sponsor.objects.create(user=user, **validated_data)