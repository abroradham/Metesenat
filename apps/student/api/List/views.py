from rest_framework.generics import ListAPIView


from apps.student.models import Student
from apps.student.api.List.serializers import StudentListSerializer

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


__all__ = ["StudentListView"]