from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админка пользователей
    """

    list_display = (
        "email",
        "type",
        "online",
        "is_verified",
        "is_active",
        "is_superuser",
        "is_staff",
    )
    list_editable = ("type",)
    list_filter = ("type",)