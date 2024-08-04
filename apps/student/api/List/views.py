from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from apps.student.models import Student
from apps.student.api.List.serializers import StudentListSerializer

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [IsAdminUser]
    search_fields = ['user__full_name']
    filterset_fields = ['type', 'university__name']


__all__ = ["StudentListView"]