from rest_framework import serializers

from apps.sponsor.models import Sponsor

class SponsorListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name")
    phone = serializers.CharField(source="user.phone")
    used_money = serializers.SerializerMethodField()

    class Meta:
        model = Sponsor
        fields = ['id', 'full_name', 'phone', "company", 'status', 'amount', 'used_money', 'created_at', 'type']

    def get_used_money(self, obj):
        return obj.used_money

