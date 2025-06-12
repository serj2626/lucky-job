from django.db import models
from django.conf import settings
from common.models import BaseDate, BaseID
from django.utils.timesince import timesince
from django.core.exceptions import ValidationError


NOTIFICATION_TYPES = (
    ("message", "Новое сообщение"),
    ("job_application", "Отклик на вакансию"),
    ("application_status", "Изменение статуса отклика"),
    ("news", "Новость"),
    ("system", "Системное уведомление"),
)


class Notification(BaseID, BaseDate):
    """Модель уведомления"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name="Пользователь",
    )
    type = models.CharField(
        "Тип уведомления", max_length=20, choices=NOTIFICATION_TYPES
    )
    title = models.CharField("Заголовок", max_length=255)
    message = models.TextField("Текст уведомления")
    is_read = models.BooleanField("Прочитано", default=False)
    payload = models.JSONField("Дополнительные данные", default=dict, blank=True)

    @property
    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_notification_type_display()} для {self.user.email}"
