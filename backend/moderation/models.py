from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class ModerationRequest(models.Model):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name="Тип"
    )
    object_id = models.PositiveIntegerField("ID объекта")
    content_object = GenericForeignKey("content_type", "object_id")

    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    reviewed = models.BooleanField(default=False, verbose_name="Проверено")
    approved = models.BooleanField(null=True, blank=True, verbose_name="Одобрено")
    comment = models.TextField("Комментарий модератора", blank=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Запрос модерации"
        verbose_name_plural = "Запросы модерации"

    def __str__(self):
        return f"{self.content_object} - {self.submitted_at}"