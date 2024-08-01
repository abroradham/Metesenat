import json
import pytest
from django.urls import reverse
from rest_framework import status


from apps.users.models import User

@pytest.mark.django_db
def test_user_login(client):
    url = reverse('user:login')
    user = User.objects.create_superuser(full_name="Abror Nematjanov", phone="913450551", password="Password")
    data = {
        "phone" : user.phone,
        "password" : "Password"
    }

    response = client.post(url, data=data, content_type='application/json')

    assert response.status_code == status.HTTP_200_OK
    assert User.objects.count() == 1
    assert response.json()["full_name"] == user.full_name
    assert response.json()["phone"] == user.phone


@pytest.mark.django_db
def test_user_login_validationerror(client):
    url = reverse('user:login')
    data = {
        "phone" : "913450551",
        "password" : "Password"
    }   

    response = client.post(url, data=data, content_type='application/json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["Error"] == ["Invalid credentials or user is not a superuser."]
