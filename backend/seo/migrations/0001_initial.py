# Generated by Django 5.1 on 2025-06-16 10:43

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RobotsTxt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="Содержимое robots.txt")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активен"),
                ),
            ],
            options={
                "verbose_name": "robots.txt",
                "verbose_name_plural": "robots.txt",
            },
        ),
        migrations.CreateModel(
            name="SEO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="URL путь, например: about/ (без начального и конечного слэша)",
                        max_length=255,
                        unique=True,
                        verbose_name="URL путь",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Макс. 60 символов",
                        max_length=255,
                        verbose_name="Заголовок (title)",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Макс. 160 символов",
                        verbose_name="Описание (meta description)",
                    ),
                ),
                (
                    "keywords",
                    models.CharField(
                        blank=True,
                        help_text="Через запятую",
                        max_length=255,
                        verbose_name="Ключевые слова (meta keywords)",
                    ),
                ),
                (
                    "canonical_url",
                    models.URLField(
                        blank=True,
                        help_text="Полный URL для canonical ссылки",
                        null=True,
                        verbose_name="Canonical URL",
                    ),
                ),
                (
                    "noindex",
                    models.BooleanField(
                        default=False,
                        help_text="Запретить индексацию страницы",
                        verbose_name="Noindex",
                    ),
                ),
                (
                    "nofollow",
                    models.BooleanField(
                        default=False,
                        help_text="Запретить переход по ссылкам на странице",
                        verbose_name="Nofollow",
                    ),
                ),
                (
                    "og_title",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="OG Заголовок"
                    ),
                ),
                (
                    "og_description",
                    models.TextField(blank=True, verbose_name="OG Описание"),
                ),
                (
                    "og_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="seo/",
                        validators=[common.validators.validate_image_extension],
                        verbose_name="OG Изображение",
                    ),
                ),
                (
                    "priority",
                    models.DecimalField(
                        decimal_places=1,
                        default=0.5,
                        help_text="От 0.1 до 1.0",
                        max_digits=2,
                        verbose_name="Приоритет в sitemap",
                    ),
                ),
                (
                    "changefreq",
                    models.CharField(
                        choices=[
                            ("always", "Всегда"),
                            ("hourly", "Каждый час"),
                            ("daily", "Ежедневно"),
                            ("weekly", "Еженедельно"),
                            ("monthly", "Ежемесячно"),
                            ("yearly", "Ежегодно"),
                            ("never", "Никогда"),
                        ],
                        default="weekly",
                        max_length=10,
                        verbose_name="Частота изменений",
                    ),
                ),
                (
                    "lastmod",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего изменения"
                    ),
                ),
                (
                    "json_ld",
                    models.TextField(
                        blank=True,
                        help_text="Дополнительная структурированная разметка",
                        verbose_name="JSON-LD разметка",
                    ),
                ),
            ],
            options={
                "verbose_name": "SEO",
                "verbose_name_plural": "SEO",
                "ordering": ["slug"],
            },
        ),
    ]
