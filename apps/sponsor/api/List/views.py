from rest_framework.generics import ListAPIView


from apps.sponsor.api.List.serializers import SponsorListSerializer
from apps.sponsor.models import Sponsor


class SponsorListView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorListSerializer



__all__ = ["SponsorListView"]