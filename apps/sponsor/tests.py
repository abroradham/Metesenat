import pytest

from apps.sponsor.models import Sponsor, SponsorShip

@pytest.mark.django_db
def test_sponsor_str_method(new_sponsor):
    assert Sponsor.__str__(new_sponsor) == new_sponsor.user.full_name


@pytest.mark.django_db
def test_sponsor_ship_str_method(new_sponsorship):
    SponsorShip.__str__(new_sponsorship) == f"{new_sponsorship.sponsor.user.full_name} sponsored to {new_sponsorship.student.user.full_name}"