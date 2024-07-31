from rest_framework import serializers

from apps.student.models import Student

class StudentListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name")
    university = serializers.CharField(source="university.name")
    dedicated_amount = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'type', 'university', 'dedicated_amount', 'tuition_fee']

    def get_dedicated_amount(self, obj):
        return obj.dedicated_amount