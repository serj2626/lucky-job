from django.db import models
import uuid
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timesince import timesince
from django.core.exceptions import ValidationError
from common.vars import CURRENCY_TYPE, MONTHS, WORK_SCHEDULE
from core.models import Category, Stack


class BaseID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseContent(models.Model):
    content = CKEditor5Field(blank=True, verbose_name="Описание", config_name="extends")

    class Meta:
        abstract = True


class BaseTitle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        abstract = True


class BaseName(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        abstract = True


class BaseDescription(models.Model):
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        abstract = True


class BaseDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


class BaseReview(BaseID, BaseDate):
    name = models.CharField("Имя", max_length=100, null=True, blank=True)
    rating = models.SmallIntegerField(
        "Рейтинг", default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField("Текст отзыва", max_length=5000, null=True, blank=True)
    verified = models.BooleanField("Проверен", default=False)

    @property
    def time_age(self):
        return timesince(self.created_at) + " назад"

    class Meta:
        abstract = True


class ResumeOrVacancyModel(BaseID, BaseDate):
    """
    Абстрактная модель для резюме и вакансий.
    """

    position = models.CharField("Должность", max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    # Зарплата
    salary_min = models.PositiveIntegerField(
        "Минимальная зарплата", null=True, blank=True
    )
    salary_max = models.PositiveIntegerField(
        "Максимальная зарплата", null=True, blank=True
    )
    currency = models.CharField(
        "Валюта", max_length=3, choices=CURRENCY_TYPE, default="RUB"
    )
    work_schedule = models.CharField(
        "График работы", max_length=200, choices=WORK_SCHEDULE, default="full-time"
    )
    skills = models.ManyToManyField(Stack, verbose_name="Стек", blank=True)

    class Meta:
        abstract = True

    def clean(self):
        if self.min_salary and self.max_salary and self.min_salary > self.max_salary:
            raise ValidationError(
                "Минимальная зарплата не может быть больше максимальной"
            )
        return super().clean()


class EducationOrExperienceModel(BaseID):
    """
    Абстрактная модель для образования или опыта.
    """

    start_month = models.CharField("Месяц начала", max_length=200, choices=MONTHS)
    start_year = models.SmallIntegerField("Год начала")
    end_month = models.CharField(
        "Месяц окончания", max_length=200, choices=MONTHS, blank=True, null=True
    )
    end_year = models.SmallIntegerField("Год окончания", blank=True, null=True)

    class Meta:
        abstract = True

    def clear(self):
        if self.start_year > self.end_year:
            raise ValidationError("Год окончания не может быть меньше года начала")
        if self.start_year == self.end_year:
            if self.start_month > self.end_month:
                raise ValidationError(
                    "Месяц окончания не может быть меньше месяца начала"
                )
            if self.start_month == self.end_month:
                raise ValidationError("Год и месяц окончания не могут быть одинаковыми")

        return super().clean()
