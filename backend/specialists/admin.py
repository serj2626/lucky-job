# from django.contrib import admin
# from .models import (
#     Specialist, SpecialistContact, SpecialistSocial, Resume,
#     Project, Experience, Education, CommentProject
# )


# class SpecialistContactInline(admin.TabularInline):
#     model = SpecialistContact
#     extra = 1


# class SpecialistSocialInline(admin.TabularInline):
#     model = SpecialistSocial
#     extra = 1


# class ResumeInline(admin.StackedInline):
#     model = Resume
#     extra = 0
#     can_delete = False


# @admin.register(Specialist)
# class SpecialistAdmin(admin.ModelAdmin):
#     list_display = ("__str__", "user", "status", "position", "gender", "date_of_birth")
#     list_filter = ("status", "gender", "skills")
#     search_fields = ("user__username", "first_name", "last_name", "position")
#     inlines = [SpecialistContactInline, SpecialistSocialInline, ResumeInline]
#     filter_horizontal = ("skills",)


# @admin.register(SpecialistContact)
# class SpecialistContactAdmin(admin.ModelAdmin):
#     list_display = ("specialist", "type", "value")
#     list_filter = ("type",)
#     search_fields = ("value", "specialist__user__username")


# @admin.register(SpecialistSocial)
# class SpecialistSocialAdmin(admin.ModelAdmin):
#     list_display = ("specialist", "type", "link")
#     list_filter = ("type",)
#     search_fields = ("link", "specialist__user__username")


# @admin.register(Resume)
# class ResumeAdmin(admin.ModelAdmin):
#     list_display = ("__str__", "specialist", "is_active")
#     list_filter = ("is_active",)
#     search_fields = ("position", "specialist__user__username")


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
