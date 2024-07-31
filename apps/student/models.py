from email.policy import default
from enum import unique
from django.db import models
from django.utils.translation import gettext_lazy as _


from apps.users.models import User
from apps.common.models import BaseModel

class University(BaseModel):
    name = models.CharField(max_length=250, null=False, blank=False, unique=True, verbose_name=_("University"))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("University")
        verbose_name_plural = _("Universities")

    
class StudenType(models.TextChoices):
    BACHELOR = "bachelor", _("Bachelor")
    MASTERS = "masters", _("Masters")


class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Student"))
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name=_("University"))
    type = models.CharField(max_length=200, choices=StudenType.choices, verbose_name=_("Type"))
    tuition_fee = models.PositiveIntegerField(default=5000, verbose_name=_("Tuition Fee"))


    @property
    def dedicated_amount(self):
        return self.sponsor.aggregate(amount=models.Sum("amount"))["amount"] or 0

    def __str__(self) -> str:
        return self.user.full_name
    

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


    @property
    def user_full_name(self):
        return self.user.full_name

    @property
    def user_phone(self):
        return self.user.phone
    
    @property
    def university_name(self):
        return self.university.name