from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser


from apps.sponsor.models import Sponsor
from apps.sponsor.api.RetrieveUpdate.serializers import SponsorDetailUpdateSerializer


class SponsorDetailUpdateview(RetrieveUpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailUpdateSerializer
    permission_classes = [IsAdminUser]



__all__ = ["SponsorDetailUpdateview"]