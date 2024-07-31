import pytest

from apps.users.models import User

@pytest.mark.django_db
def test_user_manager():
    User.objects.create_user(phone=913450551, full_name="Abror nematjanov")

    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_manager_without_phone_email():
    with pytest.raises(ValueError) as exception_info:
        User.objects.create_user(full_name="Abror Nematjanov")

    assert str(exception_info.value) == "User must have either email or phone!"

@pytest.mark.django_db
def test_user_manager_without_full_name():
    with pytest.raises(ValueError) as exception_info:
        User.objects.create_user(phone="912003112")

    assert str(exception_info.value) == "User must have a full name!"



@pytest.mark.django_db
def test_create_superuser():
    User.objects.create_superuser(phone="913450551", password="Password", full_name="Abror Nematjanov")

    assert User.objects.filter(is_superuser=True).count() == 1


@pytest.mark.django_db
def test_user_tokens():
    new_user = User.objects.create_superuser(phone="913450551", password="Password", full_name="Abror Nematjanov")

    assert User.objects.filter(is_superuser=True).count() == 1
    assert list(new_user.tokens.keys()) == ["access", "refresh"]


@pytest.mark.django_db
def test_user_str_method():
    new_user = User.objects.create_superuser(phone=913450551, full_name="Abror nematjanov", password="Password")
    assert User.__str__(new_user) == new_user.full_name


    new_user = User.objects.create(phone=882541212, full_name="Sardor nematjanov")
    assert User.__str__(new_user) == new_user.full_name

    