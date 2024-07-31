from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.db.models import Sum


from apps.sponsor.models import Sponsor
from apps.student.models import Student

class DashboardApiView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        donated_amount = Sponsor.objects.aggregate(amount=Sum("amount"))["amount"] or 0
        requested_amount = Student.objects.aggregate(amount=Sum("tuition_fee"))["amount"] or 0
        necessary_amount = requested_amount - donated_amount

        return Response(
            {
                "donated_amount" : donated_amount,
                "requested_amount" : requested_amount,
                "necessary_amount" : necessary_amount
            },
            status = status.HTTP_200_OK,
        )
    
__all__ = ["DashboardApiView"]