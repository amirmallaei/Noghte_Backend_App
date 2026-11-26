from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['phone_number', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)
