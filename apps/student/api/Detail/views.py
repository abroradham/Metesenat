from rest_framework.generics import RetrieveAPIView

from apps.student.api.Detail.serializers import StudentDetailSerializer
from apps.student.models import Student


class StudentDetailView(RetrieveAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()



__all__  = ["StudentDetailView"]