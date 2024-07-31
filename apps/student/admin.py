from django.contrib import admin

from apps.student.models import Student, University


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_full_name', 'university_name', 'user_phone', 'type',]
    search_fields = ['user_full_name']
    list_display_links = ['id', 'user_full_name']


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_display_links = ['name']