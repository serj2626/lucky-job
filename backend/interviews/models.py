from django.db import models

from companies.models import JobApplication
from common.models import BaseDate, BaseID


class Interview(BaseID, BaseDate):
    """Собеседование между кандидатом и работодателем"""

    INTERVIEW_FORMAT = (
        ("online", "Онлайн"),
        ("offline", "Офлайн"),
        ("phone", "Телефон"),
    )

    STATUS_CHOICES = (
        ("scheduled", "Запланировано"),
        ("completed", "Завершено"),
        ("cancelled", "Отменено"),
    )

    application = models.OneToOneField(
        JobApplication,
        on_delete=models.CASCADE,
        related_name="interview",
        verbose_name="Отклик",
    )

    scheduled_at = models.DateTimeField("Дата и время собеседования")
    format = models.CharField(
        "Формат", max_length=10, choices=INTERVIEW_FORMAT, default="online"
    )
    location = models.CharField("Адрес/ссылка", max_length=512, blank=True)
    notes = models.TextField("Комментарии", blank=True)

    status = models.CharField(
        "Статус", max_length=20, choices=STATUS_CHOICES, default="scheduled"
    )

    class Meta:
        verbose_name = "Собеседование"
        verbose_name_plural = "Собеседования"
        ordering = ["-scheduled_at"]

    def __str__(self):
        return f"Собеседование по {self.application.job.position} — {self.scheduled_at.strftime('%Y-%m-%d %H:%M')}"
