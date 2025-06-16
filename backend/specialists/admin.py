from django.contrib import admin
from .models import (
    Specialist,
    SpecialistContact,
    SpecialistSocial,
    Resume,
    Project,
    Experience,
    Education,
    CommentProject,
)


class SpecialistContactInline(admin.TabularInline):
    """
    Контакты специалиста
    """

    model = SpecialistContact
    extra = 1


class SpecialistSocialInline(admin.TabularInline):
    model = SpecialistSocial
    extra = 1


class ProjectInline(admin.StackedInline):
    """
    Проекты
    """

    model = Project
    extra = 0
    verbose_name = "Проект"
    verbose_name_plural = "Проекты специалиста"
    fields = (
        (
            "title",
            "category",
        ),
        (
            "link",
            "url",
        ),
        "description",
        "likes",
        "skills",
    )
    filter_horizontal = ("skills", "likes")


class ResumeInline(admin.StackedInline):
    """
    Резюме
    """

    model = Resume
    extra = 0
    can_delete = False
    verbose_name = "Резюме"
    verbose_name_plural = "Резюме специалиста"
    fields = (
        (
            "position",
            "category",
        ),
        ("salary_min", "salary_max", "currency"),
        ("work_schedule", "is_active"),
        "skills",
    )
    filter_horizontal = ("skills",)


class ExperienceInline(admin.StackedInline):
    """
    Опыт работы
    """

    model = Experience
    extra = 0
    verbose_name = "Опыт работы"
    verbose_name_plural = "Опыт работы специалиста"
    fields = (
        (
            "company",
            "category",
            "position",
        ),
        (
            "start_month",
            "start_year",
        ),
        (
            "end_month",
            "end_year",
        ),
        "description",
        "skills",
    )
    filter_horizontal = ("skills",)


class EducationInline(admin.StackedInline):
    """
    Образование
    """

    model = Education
    extra = 0
    verbose_name = "Образование"
    verbose_name_plural = "Образование специалиста"
    fields = (
        (
            "university",
            "specialization",
            "type",
        ),
        (
            "start_month",
            "start_year",
        ),
        (
            "end_month",
            "end_year",
        ),
        "file",
    )


@admin.register(Specialist)
class Admin(admin.ModelAdmin):
    """
    Админка специалистов
    """

    list_display = (
        "user",
        "status",
        "position",
        "avatar",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
    )
    list_filter = ("status", "gender", "skills")
    search_fields = ("user__username", "first_name", "last_name", "position")
    inlines = [
        EducationInline,
        ExperienceInline,
        SpecialistContactInline,
        SpecialistSocialInline,
        ResumeInline,
        ProjectInline,
    ]
    filter_horizontal = ("skills",)
    fields = (
        ("user", "status"),
        ("avatar", "position"),
        ("first_name", "last_name"),
        ("gender", "date_of_birth"),
        "skills",
    )


# class ProjectCommentInline(admin.TabularInline):
#     model = CommentProject
#     extra = 0


# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ("title", "specialist", "category", "time_ago")
#     list_filter = ("category", "skills")
#     search_fields = ("title", "description", "specialist__user__username")
#     inlines = [ProjectCommentInline]
#     filter_horizontal = ("skills", "likes")


# @admin.register(Experience)
# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ("specialist", "company", "position", "category", "start_date", "end_date")
#     list_filter = ("category", "skills")
#     search_fields = ("company", "position", "specialist__user__username")
#     filter_horizontal = ("skills",)


# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     list_display = ("specialist", "university", "specialization", "type", "start_date", "end_date")
#     list_filter = ("type",)
#     search_fields = ("university", "specialization", "specialist__user__username")


# @admin.register(CommentProject)
# class CommentProjectAdmin(admin.ModelAdmin):
#     list_display = ("project", "user", "parent", "short_text", "created_at")
#     search_fields = ("text", "user__username", "project__title")

#     def short_text(self, obj):
#         return obj.text[:75] + "..." if len(obj.text) > 75 else obj.text
#     short_text.short_description = "Комментарий"
