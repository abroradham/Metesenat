from rest_framework.generics import UpdateAPIView

from apps.sponsor.models import SponsorShip
from apps.student.api.SponsorShipUpdate.serializers import SponsorShipUpdateSerializer



class StudentSponsorshipUpdateView(UpdateAPIView):
    queryset = SponsorShip.objects.all()
    serializer_class = SponsorShipUpdateSerializer


__all__ = ["StudentSponsorshipUpdateView"]