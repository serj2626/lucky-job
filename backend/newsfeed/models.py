from django.db import models
from django.conf import settings
from common.models import BaseDate, BaseID
from django.utils.timesince import timesince
from django.core.exceptions import ValidationError


from django.db import models
from django.conf import settings
from common.models import BaseID

POST_TYPES = (
    ("job_news", "Новости вакансий"),
    ("tech_news", "Технические новости"),
    ("event", "Мероприятие"),
    ("article", "Статья"),
)


class NewsPost(BaseID):
    """Пост в ленте новостей"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="news_posts",
        verbose_name="Автор",
    )
    post_type = models.CharField("Тип поста", max_length=20, choices=POST_TYPES)
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Содержание")
    image = models.ImageField(
        "Изображение", upload_to="news_images/", null=True, blank=True
    )
    is_published = models.BooleanField("Опубликовано", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Новостной пост"
        verbose_name_plural = "Новостные посты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
