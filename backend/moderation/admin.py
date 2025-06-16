from django.contrib import admin

from .models import ModerationRequest


@admin.register(ModerationRequest)
class ModerationRequestAdmin(admin.ModelAdmin):
    list_display = ("content_object", "submitted_at", "reviewed", "approved")
    list_filter = ("reviewed", "approved")
    search_fields = ("content_type__model",)
