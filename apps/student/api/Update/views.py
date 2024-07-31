from rest_framework.generics import UpdateAPIView

from apps.student.api.Update.serializers import StudentUpdateSerializer
from apps.student.models import Student



class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer



__all__ = ["StudentUpdateView"]