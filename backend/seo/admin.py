from django.contrib import admin
from .models import SEO, RobotsTxt
from django.utils.html import format_html


@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "title",
        "noindex",
        "nofollow",
        "priority",
        "changefreq",
        "lastmod_pretty",
        "og_image_preview",
    )
    list_editable = ("noindex", "nofollow", "priority", "changefreq")
    list_filter = ("noindex", "nofollow", "changefreq")
    search_fields = ("slug", "title", "description", "keywords")
    ordering = ("slug",)

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("slug", "title", "description", "keywords")},
        ),
        ("Индексация", {"fields": ("canonical_url", "noindex", "nofollow")}),
        (
            "OpenGraph",
            {
                "fields": (
                    "og_title",
                    "og_description",
                    "og_image",
                    "og_image_preview_display",
                )
            },
        ),
        ("Sitemap", {"fields": ("priority", "changefreq", "lastmod")}),
        ("JSON-LD / Schema.org", {"fields": ("json_ld",)}),
    )

    readonly_fields = ("lastmod", "og_image_preview_display")

    def og_image_preview(self, obj):
        if obj.og_image:
            return format_html(
                '<img src="{}" style="max-height: 60px; border-radius: 4px;" />',
                obj.og_image.url,
            )
        return "—"

    og_image_preview.short_description = "OG изображение"

    def og_image_preview_display(self, obj):
        return self.og_image_preview(obj)

    def lastmod_pretty(self, obj):
        return obj.lastmod.strftime("%Y-%m-%d %H:%M")

    lastmod_pretty.short_description = "Обновлено"


# @admin.register(RobotsTxt)
# class RobotsTXTAdmin(admin.ModelAdmin):
#     list_display = ("link",)
#     fields = ("content",)

#     def link(self, obj):
#         return "Редактировать файл"

#     link.short_description = "Переход к файлу"


from django.utils.safestring import mark_safe


@admin.register(RobotsTxt)
class RobotsTxtAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active", "preview_link")
    readonly_fields = ("preview",)
    fieldsets = (
        (None, {
            "fields": ("content", "is_active", "preview")
        }),
    )

    def preview(self, obj):
        if not obj.pk:
            return "Сначала сохраните файл, чтобы просмотреть."
        url = "/robots.txt"
        return mark_safe(f'<iframe src="{url}" style="width:100%; height:200px; border:1px solid #ccc;"></iframe>')

    preview.short_description = "Предпросмотр robots.txt"

    def preview_link(self, obj):
        return mark_safe(f'<a href="/robots.txt" target="_blank">Открыть</a>')

    preview_link.short_description = "Просмотр"