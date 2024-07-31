import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_sponsor_list(client, new_sponsor, new_admin_user):
    url = reverse("sponsor:list")
    headers = {
        "Authorization" : f"Bearer {new_admin_user.tokens.get('access')}",   
    }
    response = client.get(url, HTTP_AUTHORIZATION=headers["Authorization"])
    assert response.status_code == status.HTTP_200_OK
    json_data = response.json()[0]
    
    assert list(json_data.keys()) == ["id", "full_name", "phone", "company", "status", "amount",  "used_money", "created_at", "type"]
    assert json_data["id"] == new_sponsor.id
    assert json_data["full_name"] == new_sponsor.user.full_name
    assert json_data["phone"] == new_sponsor.user.phone
    assert json_data["amount"] == new_sponsor.amount
    assert json_data["used_money"] == new_sponsor.used_money
    assert json_data["type"] == new_sponsor.type
    assert json_data["status"] == new_sponsor.status
    assert json_data["company"] == new_sponsor.company
    # print(json_data)