import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_dashboard_statistics(client, new_admin_user, new_sponsor, new_student):
    url = reverse("sponsor:dashboard")
    headers = {
        "Authorization" : f"Bearer {new_admin_user.tokens.get('access')}",   
    }
    response = client.get(url, HTTP_AUTHORIZATION=headers["Authorization"])
    assert response.status_code ==  status.HTTP_200_OK
    assert list(response.json().keys()) == ["donated_amount", "requested_amount", "necessary_amount"]
    assert response.json()["donated_amount"] == new_sponsor.amount
    assert response.json()["requested_amount"] == new_student.tuition_fee
    assert response.json()["necessary_amount"] == new_student.tuition_fee - new_sponsor.amount