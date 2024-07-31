import factory

from apps.users.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    full_name = factory.Faker("word")
    phone = factory.Faker("phone_number")
    email = factory.Faker("email")


class SuperUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    full_name = factory.Faker("word")
    phone = factory.Faker("phone_number")
    email = factory.Faker("email")
    password = "Password"
    is_active = True
    is_staff = True
    is_superuser = True


__all__ = ["UserFactory", "SuperUserFactory"]