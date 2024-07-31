from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "full_name", "is_staff")
    list_filter = ("is_staff", "created_at")
    search_fields = ("id", "phone",  "first_name", "last_name", "username", 'full_name')
