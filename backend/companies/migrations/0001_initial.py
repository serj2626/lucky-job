# Generated by Django 5.1 on 2025-06-12 09:34

import common.mixins
import common.upload_to
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=common.upload_to.dynamic_upload_to,
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название компании"),
                ),
                (
                    "legal_name",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("OOO", "ООО"),
                            ("IP", "ИП"),
                            ("UP", "УП"),
                            ("PAO", "ПАО"),
                            ("Corp", "Corp"),
                            ("ZAO", "ЗАО"),
                            ("OAO", "ОАО"),
                            ("AO", "АО"),
                            ("other", "Другое"),
                        ],
                        max_length=255,
                        null=True,
                        verbose_name="Юридическое название",
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                ("website", models.URLField(blank=True, verbose_name="Сайт")),
                (
                    "is_verified",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Проверенная компания"
                    ),
                ),
                (
                    "founded_year",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Год основания"
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("1-10", "1-10 сотрудников"),
                            ("11-50", "11-50 сотрудников"),
                            ("51-200", "51-200 сотрудников"),
                            ("201-500", "201-500 сотрудников"),
                            ("501+", "Более 500 сотрудников"),
                        ],
                        max_length=10,
                        verbose_name="Размер компании",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="company",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Компания",
                "verbose_name_plural": "Компании",
                "ordering": ["name"],
            },
            bases=(models.Model, common.mixins.WebpImageMixin),
        ),
        migrations.CreateModel(
            name="CompanyContact",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("phone", "Телефон"),
                            ("email", "Почта"),
                            ("skype", "Skype"),
                            ("country", "Страна"),
                            ("city", "Город"),
                            ("address", "Адрес"),
                            ("other", "Другое"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Имя контакта",
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Значение"
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contacts",
                        to="companies.company",
                        verbose_name="Компания",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт компании",
                "verbose_name_plural": "Контакты компании",
            },
        ),
        migrations.CreateModel(
            name="CompanySocial",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("vk", "VK"),
                            ("tg", "Telegram"),
                            ("insta", "Instagram"),
                            ("facebook", "Facebook"),
                            ("linkedin", "LinkedIn"),
                            ("twitter", "Twitter"),
                            ("other", "Другое"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Тип социальной сети",
                    ),
                ),
                ("link", models.URLField(blank=True, null=True, verbose_name="Ссылка")),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="socials",
                        to="companies.company",
                        verbose_name="Компания",
                    ),
                ),
            ],
            options={
                "verbose_name": "Социальная сеть компании",
                "verbose_name_plural": "Социальные сети компании",
            },
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                (
                    "position",
                    models.CharField(max_length=200, verbose_name="Должность"),
                ),
                (
                    "salary_min",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Минимальная зарплата"
                    ),
                ),
                (
                    "salary_max",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Максимальная зарплата"
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[("RUB", "руб"), ("USD", "долл"), ("EUR", "евро")],
                        default="RUB",
                        max_length=3,
                        verbose_name="Валюта",
                    ),
                ),
                (
                    "work_schedule",
                    models.CharField(
                        choices=[
                            ("project", "Проектная работа"),
                            ("full_time", "Полная занятость"),
                            ("part_time", "Частичная занятость"),
                            ("temporary", "Временная работа"),
                            ("internship", "Стажировка"),
                        ],
                        default="full-time",
                        max_length=200,
                        verbose_name="График работы",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание вакансии")),
                (
                    "requirements",
                    models.TextField(blank=True, verbose_name="Требования"),
                ),
                (
                    "responsibilities",
                    models.TextField(blank=True, verbose_name="Обязанности"),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("none", "Не имеет значения"),
                            ("intern", "Стажер"),
                            ("junior", "Junior"),
                            ("junior_plus", "Junior+"),
                            ("middle", "Middle"),
                            ("middle_plus", "Middle+"),
                            ("senior", "Senior"),
                            ("team_lead", "Team Lead"),
                        ],
                        default="junior",
                        max_length=200,
                        verbose_name="Уровень",
                    ),
                ),
                (
                    "format_work",
                    models.CharField(
                        choices=[
                            ("office", "В офисе"),
                            ("remote", "Удаленная работа"),
                            ("hybrid", "Гибридная работа"),
                        ],
                        default="remote",
                        max_length=20,
                        verbose_name="Формат работы",
                    ),
                ),
                (
                    "experience",
                    models.CharField(
                        choices=[
                            ("no_exp", "Без опыта"),
                            ("1-3", "1-3 года"),
                            ("3-5", "3-5 лет"),
                            ("5+", "Более 5 лет"),
                        ],
                        default="no_exp",
                        max_length=10,
                        verbose_name="Требуемый опыт",
                    ),
                ),
                (
                    "education",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("none", "Не требуется"),
                            ("secondary", "Среднее образование"),
                            ("master", "Высшее образование"),
                        ],
                        default="none",
                        max_length=20,
                        null=True,
                        verbose_name="Образование",
                    ),
                ),
                (
                    "country",
                    models.CharField(blank=True, max_length=100, verbose_name="Страна"),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=100, verbose_name="Город"),
                ),
                (
                    "address",
                    models.CharField(blank=True, max_length=255, verbose_name="Адрес"),
                ),
                (
                    "hide_salary",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Скрыть зарплату"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активная вакансия"),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancies",
                        to="companies.company",
                        verbose_name="Компания",
                    ),
                ),
                (
                    "skills",
                    models.ManyToManyField(
                        blank=True, to="core.stack", verbose_name="Стек"
                    ),
                ),
            ],
            options={
                "verbose_name": "Вакансия",
                "verbose_name_plural": "Вакансии",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="JobApplication",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "cover_letter",
                    models.TextField(
                        blank=True, verbose_name="Сопроводительное письмо"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "На рассмотрении"),
                            ("reviewed", "Просмотрено"),
                            ("interview", "Приглашение на интервью"),
                            ("rejected", "Отклонено"),
                            ("hired", "Принято"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="Статус отклика",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата отклика"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_applications",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Соискатель",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="companies.job",
                        verbose_name="Вакансия",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отклик на вакансию",
                "verbose_name_plural": "Отклики на вакансии",
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddIndex(
            model_name="job",
            index=models.Index(
                fields=["position"], name="companies_j_positio_8c3a35_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="job",
            index=models.Index(
                fields=["is_active"], name="companies_j_is_acti_36e9d1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="job",
            index=models.Index(
                fields=["company"], name="companies_j_company_2622f6_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="jobapplication",
            unique_together={("job", "applicant")},
        ),
    ]
