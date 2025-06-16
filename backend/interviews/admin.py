from django.contrib import admin

from .models import Interview


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("application", "scheduled_at", "format", "status")
    list_filter = ("format", "status")
    search_fields = ("application__job__position", "application__specialist__email")
