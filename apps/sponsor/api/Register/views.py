from rest_framework.generics import CreateAPIView

from apps.sponsor.api.Register.serializers import SponsorCreateSerializer
from apps.sponsor.models import Sponsor


class SponsorRegisterView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer


__all__  = ["SponsorRegisterView"]
