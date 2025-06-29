from django.contrib import admin
from .models import (
    Company,
    CompanySocial,
    CompanyContact,
    Job,
    JobApplication,
)


class JobInline(admin.StackedInline):
    model = Job
    extra = 0

    verbose_name = "Вакансия"
    verbose_name_plural = "Вакансии"
    fields = (
        (
            "position",
            "category",
            "is_active",
        ),
        ("level", "format_work", ),
        ("experience", "education", ),
        ("country", "city", ),
        ("address", "hide_salary", ),
        ("salary_min", "salary_max", "currency"),
        "work_schedule",
        "description",
        "requirements",
        "responsibilities",
        "skills",
    )

    filter_horizontal = ("skills",)


class CompanySocialInline(admin.TabularInline):
    model = CompanySocial
    extra = 0


class CompanyContactInline(admin.TabularInline):
    model = CompanyContact
    extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Админка компаний
    """

    list_display = (
        "user",
        "avatar",
        "name",
        "legal_name",
        "website",
        "is_verified",
        "founded_year",
        "size",
    )
    fields = (
        (
            "name",
            "legal_name",
        ),
        ("website", "avatar"),
        ("is_verified", "founded_year", "size"),
        "description",
    )
    inlines = (JobInline, CompanyContactInline, CompanySocialInline)


# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ("name", "legal_name", "user", "is_verified", "founded_year", "size")
#     list_filter = ("is_verified", "size", "legal_name")
#     search_fields = ("name", "user__email", "description")
#     readonly_fields = ("id",)
#     ordering = ("name",)


# @admin.register(CompanySocial)
# class CompanySocialAdmin(admin.ModelAdmin):
#     list_display = ("company", "name", "link")
#     list_filter = ("name",)
#     search_fields = ("company__name", "link")
#     autocomplete_fields = ("company",)


# @admin.register(CompanyContact)
# class CompanyContactAdmin(admin.ModelAdmin):
#     list_display = ("company", "name", "value", "created_at")
#     list_filter = ("name",)
#     search_fields = ("company__name", "value")
#     autocomplete_fields = ("company",)


# @admin.register(Job)
# class JobAdmin(admin.ModelAdmin):
#     list_display = (
#         "position",
#         "company",
#         "level",
#         "format_work",
#         "experience",
#         "education",
#         "is_active",
#         "views_count",
#     )
#     list_filter = (
#         "is_active",
#         "level",
#         "format_work",
#         "experience",
#         "education",
#         "company",
#     )
#     search_fields = ("position", "company__name", "description")
#     readonly_fields = ("views_count", "created_at", "updated_at")
#     autocomplete_fields = ("company",)
#     ordering = ("-created_at",)


# @admin.register(JobApplication)
# class JobApplicationAdmin(admin.ModelAdmin):
#     list_display = ("job", "specialist", "status", "created_at")
#     list_filter = ("status", "created_at")
#     search_fields = ("job__position", "specialist__email", "cover_letter")
#     autocomplete_fields = ("job", "specialist")
#     ordering = ("-created_at",)
