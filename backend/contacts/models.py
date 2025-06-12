from django.db import models
from django.contrib.auth import get_user_model
from common.upload_to import dynamic_upload_to
from django.utils.timesince import timesince


TYPE_FEEDBACK = (
    ("question", "Вопрос"),
    ("suggestion", "Предложение"),
    ("complaint", "Жалоба"),
)

User = get_user_model()


class Subscription(models.Model):
    """Модель подписки."""

    email = models.EmailField("Почта", max_length=254, unique=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)

    def __str__(self):
        return f"Подписка на новости  от {self.email}"

    class Meta:

        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Feedback(models.Model):
    """Модель обратной связи."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    subject = models.CharField(
        "Тема", max_length=200, choices=TYPE_FEEDBACK, default="question"
    )
    text = models.TextField("Сообщение", max_length=1000)
    photo = models.FileField("Фото", upload_to=dynamic_upload_to, blank=True, null=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)

    @property
    def time_ago(self):
        return timesince(self.created_at)

    def __str__(self):
        return f"Обратная связь от {self.user.email}"

    class Meta:

        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
