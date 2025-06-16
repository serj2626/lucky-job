from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from common.mixins import WebpImageMixin
from common.upload_to import dynamic_upload_to
from core.models import Category, Stack
from django.utils.timesince import timesince

from common.models import (
    BaseDate,
    BaseID,
    EducationOrExperienceModel,
    ResumeOrVacancyModel,
)
from django.core.validators import MinValueValidator, MaxValueValidator
from common.vars import SOCIAL_TYPES, CONTACT_TYPES

User = get_user_model()


STATUS_EMPLOYEE = (
    ("unemployed", "Не ищу работу"),
    ("search", "В поиске работы"),
)

TYPE_GENDER = (
    ("male", "Мужской"),
    ("female", "Женский"),
    ("other", "Другое"),
)

TYPE_EDUCATION = (
    ("course", "Курс"),
    ("college", "Колледж"),
    ("univer", "Университет"),
)


class Specialist(BaseID, WebpImageMixin):
    """Модель работника."""

    image_field_name = "avatar"

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    status = models.CharField(
        choices=STATUS_EMPLOYEE, max_length=300, default="search", verbose_name="Статус"
    )
    position = models.CharField("Должность", max_length=300, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=dynamic_upload_to, null=True, blank=True, verbose_name="Аватар"
    )
    skills = models.ManyToManyField(Stack, verbose_name="Стек", blank=True)
    first_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Фамилия"
    )
    gender = models.CharField(
        max_length=255, choices=TYPE_GENDER, default="other", verbose_name="Пол"
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения"
    )

    def clean(self):
        super().clean()
        if self.date_of_birth:
            if self.date_of_birth > timezone.now().date():
                raise ValidationError(
                    {"date_of_birth": "Дата рождения не может быть в будущем"}
                )
            if (timezone.now().date() - self.date_of_birth).days < 16 * 365:
                raise ValidationError(
                    {"date_of_birth": "Работник должен быть старше 16 лет"}
                )

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self):
        name = f"{self.first_name or ''} {self.last_name or ''}".strip()
        return f"Специалист {name or self.user.email}"


class SpecialistContact(models.Model):
    """
    Модель контактов специалиста
    """

    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, verbose_name="Специалист"
    )
    type = models.CharField(
        choices=CONTACT_TYPES, max_length=300, verbose_name="Тип контакта"
    )
    value = models.CharField(max_length=300, verbose_name="Значение")

    class Meta:
        verbose_name = "Контакт специалиста"
        verbose_name_plural = "Контакты специалистов"

    def __str__(self):
        return f"Контакт специалиста: {self.value}"


class SpecialistSocial(models.Model):
    """
    Модель социальных сетей специалиста
    """

    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, verbose_name="Специалист"
    )
    type = models.CharField(
        choices=SOCIAL_TYPES, max_length=300, verbose_name="Тип социальной сети"
    )
    link = models.URLField("Ссылка", null=True, blank=True)

    class Meta:
        verbose_name = "Социальная сеть специалиста"
        verbose_name_plural = "Социальные сети специалистов"

    def __str__(self):
        return f"Социальная сеть специалиста: {self.get_type_display()}"


class Resume(ResumeOrVacancyModel):
    """Модель резюме специалиста."""

    specialist = models.OneToOneField(
        Specialist,
        on_delete=models.CASCADE,
        related_name="resume",
        verbose_name="Специалист",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активное резюме")

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return f"Резюме: {self.position} ({self.specialist})"


class Project(BaseID, BaseDate, WebpImageMixin):
    """Модель проекта."""

    image_field_name = "poster"

    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="Специалист",
    )
    title = models.CharField("Название проекта", max_length=300)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория"
    )
    poster = models.ImageField(
        "Постер", upload_to=dynamic_upload_to, blank=True, null=True
    )
    likes = models.ManyToManyField(
        User, verbose_name="Лайки", blank=True, related_name="+"
    )
    skills = models.ManyToManyField(Stack, verbose_name="Стек", blank=True)
    link = models.URLField("Ссылка на код проекта", blank=True, null=True)
    url = models.URLField("Ссылка на проект", blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)

    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"Проект {self.title} специалиста {self.employee}"


class Experience(EducationOrExperienceModel):
    """Модель опыта работы."""

    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        verbose_name="Специалист",
        related_name="experiences",
    )
    company = models.CharField("Компания", max_length=300)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория"
    )
    skills = models.ManyToManyField(Stack, verbose_name="Стек")
    position = models.CharField("Должность", max_length=200)
    description = models.TextField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return f"Опыт работы {self.specialist} в {self.company}"


class Education(EducationOrExperienceModel):
    """Модель образования."""

    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        verbose_name="Работник",
        related_name="educations",
    )
    type = models.CharField(
        "Тип", max_length=300, choices=TYPE_EDUCATION, default="univer"
    )
    university = models.CharField("Университет", max_length=300)
    specialization = models.CharField("Специализация", max_length=300)
    file = models.FileField(
        "Диплом или сертификат", upload_to=dynamic_upload_to, null=True, blank=True
    )

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def __str__(self):
        return f"Образование {self.employee} в {self.university}"


class CommentProject(BaseDate):
    """
    Модель комментария к проекту.
    """

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Проект",
        related_name="comments",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="comments_by_project",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Родительский комментарий",
        blank=True,
        null=True,
    )
    text = models.TextField("Текст комментария", max_length=5000)

    @property
    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Комментарий к проекту"
        verbose_name_plural = "Комментарии к проекту"

    def __str__(self):
        return f"Комментарий к проекту {self.project}"


# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_company_profile(sender, instance, created, **kwargs):
#     if created and instance.type == "specialist":
#         Specialist.objects.create(user=instance)
