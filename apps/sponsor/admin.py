from django.contrib import admin

from apps.sponsor.models import Sponsor, SponsorShip
# Register your models here.

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):

    list_display = ['id', 'user_full_name', 'user_phone', 'type', 'company', 'amount']
    search_fields = ['user_full_name', 'user_phone']


admin.site.register(SponsorShip)
