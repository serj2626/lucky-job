from django.contrib import admin
from .models import (
    Category,
    Stack,
)


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    """
    Админка стеков
    """

    list_display = ("name", "slug")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Админка категорий
    """

    list_display = (
        "name",
        "slug",
    )