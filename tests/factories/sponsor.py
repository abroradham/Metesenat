import factory

from apps.sponsor.models import SponsorStatus, SponsorType, Sponsor, SponsorShip


class SponsorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sponsor


    user = factory.SubFactory("tests.factories.user.UserFactory")
    type = SponsorType.INDIVIDUAL
    status = SponsorStatus.IN_MODERATION
    amount = factory.Faker("pyint", min_value=2000)
    company = factory.Faker("company")



class SponsorShipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SponsorShip


    sponsor = factory.SubFactory("tests.factories.sponsor.SponsorFactory")
    student = factory.SubFactory("tests.factories.student.StudentFactory")
    amount = factory.Faker("pyint", max_value=500)



__all__ = ["SponsorFactory", "SponsorShipFactory"]