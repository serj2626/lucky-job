# Generated by Django 5.1 on 2025-06-16 10:43

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cookie",
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
                    "content",
                    django_ckeditor_5.fields.CKEditor5Field(
                        blank=True, verbose_name="Описание"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Политика cookie",
                "verbose_name_plural": "Политика cookie",
            },
        ),
        migrations.CreateModel(
            name="Offerta",
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
                    "content",
                    django_ckeditor_5.fields.CKEditor5Field(
                        blank=True, verbose_name="Описание"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Оферта",
                "verbose_name_plural": "Оферта",
            },
        ),
        migrations.CreateModel(
            name="Policy",
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
                    "content",
                    django_ckeditor_5.fields.CKEditor5Field(
                        blank=True, verbose_name="Описание"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Политика конфиденциальности",
                "verbose_name_plural": "Политика конфиденциальности",
            },
        ),
    ]
