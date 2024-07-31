from rest_framework.generics import CreateAPIView

from apps.student.api.Create.serializers import StudentCreateSerializer
from apps.student.models import Student


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer



__all__ = ["StudentCreateView"]