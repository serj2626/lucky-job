from django.db import models

from common.models import BaseContent, BaseTitle

class Offerta(BaseTitle, BaseContent):
    """
    Оферта
    """

    class Meta:
        verbose_name = "Оферта"
        verbose_name_plural = "Оферта"

    def __str__(self):
        return f'Оферта "{self.title}"'


class Policy(BaseTitle, BaseContent):
    """
    Политика конфиденциальности
    """

    class Meta:
        verbose_name = "Политика конфиденциальности"
        verbose_name_plural = "Политика конфиденциальности"

    def __str__(self):
        return f"Политика конфиденциальности '{self.title}'"


class Cookie(BaseTitle, BaseContent):
    """
    Политика cookie
    """

    class Meta:
        verbose_name = "Политика cookie"
        verbose_name_plural = "Политика cookie"

    def __str__(self):
        return f'Политика cookie "{self.title}"'

    class Meta:
        verbose_name = "Политика cookie"
        verbose_name_plural = "Политика cookie"

