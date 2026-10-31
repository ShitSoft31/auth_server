"""Django admin registration for the central User model."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Reuses Django's user admin and only appends ShitSoft-specific fields.

    Inheriting the default fieldsets guarantees that username/password
    management keeps behaving exactly like Django's built-in User model.
    """

    fieldsets = BaseUserAdmin.fieldsets + (("ShitSoft Profile", {"fields": ("bio",)}),)
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("ShitSoft Profile", {"fields": ("bio",)}),
    )
    list_display = BaseUserAdmin.list_display + ("bio",)
