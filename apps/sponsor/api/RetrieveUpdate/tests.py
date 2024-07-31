import pytest
from django.urls import reverse
from rest_framework import status

from apps.sponsor.models import Sponsor, SponsorStatus, SponsorType


@pytest.mark.django_db
def test_sponsor_update(client, new_admin_user, new_sponsor):
    url = reverse("sponsor:update", kwargs={"pk": new_sponsor.id})
    headers = {
        "Authorization" : f"Bearer {new_admin_user.tokens.get("access")}",   
    }
    response = client.get(url, HTTP_AUTHORIZATION=headers["Authorization"])
    sponsor_data = {
        "user" : {"full_name" : "New_full_name", 'phone' : "882541212"},
        "type" : SponsorType.LEGAL,
        "amount" : 5000
    }

    response = client.patch(url, data=sponsor_data, content_type="application/json", HTTP_AUTHORIZATION=headers["Authorization"])

    assert response.json()["id"] == new_sponsor.id
    assert response.json()["user"] == sponsor_data["user"]
    assert response.json()["type"] == sponsor_data["type"]
    assert response.json()["amount"] == sponsor_data["amount"]