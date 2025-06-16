from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("email", "type", "is_staff", "is_superuser", )
    search_fields = ("email","type" )
    ordering = ("email","type")
    # inlines = (ProfileLine,)

    # def has_profile(self, obj):
    #     return hasattr(obj, "profile")

    # has_profile.boolean = True
    # has_profile.short_description = "Профиль есть?"
