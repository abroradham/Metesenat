from urllib import response
import pytest
from django.urls import reverse
from rest_framework import status

from apps.sponsor.models import Sponsor, SponsorType


@pytest.mark.django_db
def test_sponsor_register(client):
    url = reverse("sponsor:register")
    sponsor_data = {
        "user" : {"full_name" : "Abror Nematjanov", "phone" : "913450551"},
        "type" : SponsorType.LEGAL,
        "amount" : 2000
    }

    response = client.post(url, data=sponsor_data, content_type="application/json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Sponsor.objects.count() == 1


@pytest.mark.django_db
def test_sponsor_register_validation(client):
    url = reverse("sponsor:register")
    sponsor_data = {
        "user" : {"full_name" : "Abror Nematjanov", "phone" : "913450551"},
        "type" : SponsorType.INDIVIDUAL,
        "amount" : 2000
    }

    response = client.post(url, data=sponsor_data, content_type="application/json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "company" in response.json()
    assert response.json()["company"] == ["This field is required for individual sponsors"]