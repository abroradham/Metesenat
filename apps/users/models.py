from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.models import BaseModel
from .managers import CustomUserManager

class User(AbstractUser, BaseModel):
    
    full_name = models.CharField(_("Full Name"), max_length=250, null=False, blank=False,)
    username = None
    phone = models.CharField(_("Phone"), max_length=13, null=True, blank=True, unique=True)
    email = models.EmailField(_("Email"), max_length=200, null=True, blank=True, unique=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.full_name 
    
    @property
    def tokens(self):
        token = RefreshToken.for_user(self)
        return {"access" : str(token.access_token), "refresh" : str(token)}
    

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")