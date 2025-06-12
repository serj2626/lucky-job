# models.py
from django.db import models
from django.conf import settings
from common.upload_to import dynamic_upload_to
from common.mixins import WebpImageMixin
from common.vars import (
    FORMAT_WORK,
    LEVELS_REQUIREMENTS,
    SOCIAL_TYPES,
    CONTACT_TYPES,
)
from django.core.validators import MinValueValidator, MaxValueValidator
from common.models import BaseDate, BaseID, ResumeOrVacancyModel
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

COMPANY_TYPES = (
    ("OOO", "ООО"),
    ("IP", "ИП"),
    ("UP", "УП"),
    ("PAO", "ПАО"),
    ("Corp", "Corp"),
    ("ZAO", "ЗАО"),
    ("OAO", "ОАО"),
    ("AO", "АО"),
    ("other", "Другое"),
)

EXPERIENCE_LEVELS = (
    ("no_exp", "Без опыта"),
    ("1-3", "1-3 года"),
    ("3-5", "3-5 лет"),
    ("5+", "Более 5 лет"),
)

EDUCATION_LEVELS = (
    ("none", "Не требуется"),
    ("secondary", "Среднее образование"),
    ("master", "Высшее образование"),
)


class Company(BaseID, WebpImageMixin):
    """Модель компании/работодателя"""

    image_field_name = "avatar"

    COMPANY_SIZE_CHOICES = (
        ("1-10", "1-10 сотрудников"),
        ("11-50", "11-50 сотрудников"),
        ("51-200", "51-200 сотрудников"),
        ("201-500", "201-500 сотрудников"),
        ("501+", "Более 500 сотрудников"),
    )

    # Связь с пользователем
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="company",
        verbose_name="Пользователь",
    )
    avatar = models.ImageField(
        upload_to=dynamic_upload_to, null=True, blank=True, verbose_name="Аватар"
    )

    # Основная информация
    name = models.CharField("Название компании", max_length=255)
    legal_name = models.CharField(
        "Юридическое название",
        max_length=255,
        choices=COMPANY_TYPES,
        blank=True,
        null=True,
    )
    description = models.TextField("Описание", blank=True)
    website = models.URLField("Сайт", blank=True)
    is_verified = models.BooleanField("Проверенная компания", default=False, blank=True)
    founded_year = models.PositiveIntegerField("Год основания", null=True, blank=True)
    size = models.CharField(
        "Размер компании", max_length=10, choices=COMPANY_SIZE_CHOICES, blank=True
    )

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"Компания {self.legal_name} - {self.user.email}"
        super().save(*args, **kwargs)

    @property
    def display_size(self):
        return dict(self.COMPANY_SIZE_CHOICES).get(self.size, "Не указано")

    def increment_job_count(self):
        self.jobs_posted = models.F("jobs_posted") + 1
        self.save(update_fields=["jobs_posted"])


class CompanySocial(BaseID):
    """
    Модель социальных сетей компании
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="socials",
        verbose_name="Компания",
    )
    name = models.CharField(
        "Тип социальной сети",
        choices=SOCIAL_TYPES,
        max_length=100,
        null=True,
        blank=True,
    )
    link = models.URLField("Ссылка", null=True, blank=True)

    def __str__(self):
        return f"{self.company.user.email} - {self.get_name_display()}"

    class Meta:
        verbose_name = "Социальная сеть компании"
        verbose_name_plural = "Социальные сети компании"


class CompanyContact(BaseID, BaseDate):
    """
    Модель контактов компании
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name="Компания",
    )
    name = models.CharField(
        "Имя контакта", choices=CONTACT_TYPES, max_length=100, null=True, blank=True
    )
    value = models.CharField("Значение", max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.company.user.email} -  {self.get_name_display()}"

    class Meta:
        verbose_name = "Контакт компании"
        verbose_name_plural = "Контакты компании"


class Job(ResumeOrVacancyModel):
    """Модель вакансии"""

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="vacancies",
        verbose_name="Компания",
    )

    # Основная информация
    description = models.TextField("Описание вакансии")
    requirements = models.TextField("Требования", blank=True)
    responsibilities = models.TextField("Обязанности", blank=True)
    level = models.CharField(
        "Уровень", max_length=200, choices=LEVELS_REQUIREMENTS, default="junior"
    )
    format_work = models.CharField(
        "Формат работы", max_length=20, choices=FORMAT_WORK, default="remote"
    )
    # Опыт и образование
    experience = models.CharField(
        "Требуемый опыт", max_length=10, choices=EXPERIENCE_LEVELS, default="no_exp"
    )
    education = models.CharField(
        "Образование",
        max_length=20,
        choices=EDUCATION_LEVELS,
        default="none",
        blank=True,
        null=True,
    )

    # Локация
    country = models.CharField("Страна", max_length=100, blank=True)
    city = models.CharField("Город", max_length=100, blank=True)
    address = models.CharField("Адрес", max_length=255, blank=True)
    hide_salary = models.BooleanField("Скрыть зарплату", default=False, blank=True)

    is_active = models.BooleanField("Активная вакансия", default=True)
    views_count = models.PositiveIntegerField("Количество просмотров", default=0)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["position"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["company"]),
        ]

    def __str__(self):
        return f"{self.position} в {self.company.name}"

    @property
    def salary_range(self):
        if self.hide_salary:
            return "По договоренности"
        if self.salary_min and self.salary_max:
            return f"{self.salary_min:,} - {self.salary_max:,} {self.get_currency_display()}"
        if self.salary_min:
            return f"от {self.salary_min:,} {self.get_currency_display()}"
        if self.salary_max:
            return f"до {self.salary_max:,} {self.get_currency_display()}"
        return "По договоренности"

    def increment_views(self):
        self.views_count = models.F("views_count") + 1
        self.save(update_fields=["views_count"])


class JobApplication(BaseID, BaseDate):
    """Модель отклика на вакансию"""

    STATUS_CHOICES = (
        ("pending", "На рассмотрении"),
        ("reviewed", "Просмотрено"),
        ("interview", "Приглашение на интервью"),
        ("rejected", "Отклонено"),
        ("hired", "Принято"),
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name="Вакансия",
    )
    specialist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="job_applications",
        verbose_name="Соискатель",
    )
    cover_letter = models.TextField("Сопроводительное письмо", blank=True)
    status = models.CharField(
        "Статус отклика", max_length=20, choices=STATUS_CHOICES, default="pending"
    )

    class Meta:
        verbose_name = "Отклик на вакансию"
        verbose_name_plural = "Отклики на вакансии"
        unique_together = ("job", "specialist")
        ordering = ["-created_at"]

    def __str__(self):
        return f"Отклик {self.applicant.email} на {self.job.position} в {self.job.company.name}"


# Сигналы для автоматического создания профиля компании
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_company_profile(sender, instance, created, **kwargs):
    if created and instance.type == "company":
        Company.objects.create(user=instance)
