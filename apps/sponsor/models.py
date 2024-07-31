from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.student.models import Student
from apps.users.models import User
from apps.common.models import BaseModel


class SponsorStatus(models.TextChoices):
    NEW = "new", _("New")
    IN_MODERATION = "in_moderation", _("In Moderation")
    DECLINED = "declined", _("Declined")
    ACCEPTED = "accepted", _("Accepted")


class SponsorType(models.TextChoices):
    LEGAL = "legal", _("Legal")
    INDIVIDUAL = "individual", _("Individual")

class Sponsor(BaseModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    type = models.CharField(max_length=200, default=SponsorType.LEGAL, choices=SponsorType.choices, verbose_name=_("Type")) 
    status = models.CharField(max_length=200, default=SponsorStatus.NEW, choices=SponsorStatus.choices, verbose_name=_("Status"))
    amount = models.PositiveIntegerField(default=5000, verbose_name=_("Amount"))
    company = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Company"))


    @property
    def left_money(self):
        sponsored_amount = self.sponsorship.aggregate(amount=models.Sum("amount"))["amount"] or 0
        return self.amount - sponsored_amount
    
    @property
    def used_money(self):
        return self.sponsorship.aggregate(amount=models.Sum("amount"))["amount"] or 0
    
    @property
    def user_full_name(self):
        return self.user.full_name

    @property
    def user_phone(self):
        return self.user.phone



    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")



class SponsorShip(BaseModel):
    
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name="sponsorship", verbose_name=_('Sponsor'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="sponsor", verbose_name=_('Student'))
    amount = models.PositiveIntegerField(default=5000, verbose_name=_('Amount'))

    def __str__(self) -> str:
        return f"{self.sponsor.user.full_name} sponsored to {self.student.user.full_name}"
    
    def clean(self) -> None:
        if self.sponsor.left_money < self.amount:
            raise ValidationError("Sponsor does not have enough money")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("SponsorShip")
        verbose_name_plural = _("SponsorShips")
