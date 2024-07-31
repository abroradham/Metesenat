from rest_framework import serializers

from apps.sponsor.models import SponsorShip


class SponsorShipUpdateSerializer(serializers.ModelSerializer):
    sponsor_name = serializers.CharField(source="sponsor.user.full_name")


    class Meta:
        model = SponsorShip
        fields = ("id", "amount", "sponsor_name")