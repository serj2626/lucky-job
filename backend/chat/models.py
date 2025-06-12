from django.db import models
from django.conf import settings
from common.models import BaseDate, BaseID
from django.utils.timesince import timesince
from django.core.exceptions import ValidationError


class Chat(BaseID, BaseDate):
    """Диалог между пользователем и компанией"""

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="conversations", verbose_name="Участники"
    )
    job = models.ForeignKey(
        "companies.Job",
        on_delete=models.CASCADE,
        related_name="conversations",
        null=True,
        blank=True,
        verbose_name="Связанная вакансия",
    )

    @property
    def time_ago(self):
        return timesince(self.created_at)

    def clean(self):
        if self.users.count() != 2:
            raise ValidationError("Диалог должен состоять из двух пользователей")
        return super().clean()

    class Meta:
        verbose_name = "Диалог"
        verbose_name_plural = "Диалоги"
        ordering = ["-updated_at"]

    def __str__(self):
        return f"Диалог {self.id}"



class Message(BaseID, BaseDate):
    """Сообщение в диалоге"""

    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Диалог",
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages",
        verbose_name="Отправитель",
    )
    content = models.TextField("Текст сообщения")
    is_read = models.BooleanField("Прочитано", default=False)

    @property
    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["timestamp"]

    def __str__(self):
        return f"Сообщение от {self.sender.email}"
