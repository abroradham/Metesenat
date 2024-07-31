import factory

from apps.student.models import Student, StudenType

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory("tests.factories.user.UserFactory")
    university = factory.SubFactory("tests.factories.university.UniversityFactory")
    type = StudenType.BACHELOR
    tuition_fee = factory.Faker("pyint", min_value=500)



    __all__ = ["StudentFactory"]
