from django.utils.html import format_html
from django.utils.safestring import mark_safe
from PIL import Image
import io
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.core.exceptions import MultipleObjectsReturned

from common.upload import compress_image


class AvatarPreviewMixin:
    """
    Данный миксин отображает превью аватара в админке.
    Его нужно использовать в модели, у которых есть изображение
    """

    image_field_name = "avatar"

    def avatar_preview(self):
        avatar = getattr(self, self.image_field_name, None)
        if avatar:
            return format_html(
                '<img src="{}" style="max-height: 200px;" />', avatar.url
            )
        return "Нет изображения"

    avatar_preview.short_description = "Превью аватара"


class WebpImageMixin:
    """
    Миксин для сжатия изображений
    """

    image_field_name = "image"

    def save(self, *args, **kwargs):
        if hasattr(self, self.image_field_name):
            image_field = getattr(self, self.image_field_name)
            if image_field:
                image_field = compress_image(image_field)
                setattr(self, self.image_field_name, image_field)
        super().save(*args, **kwargs)


class AdminImagePreviewMixin:
    """
    Миксин для отображения изображений в админке
    """

    image_field_name = "image"

    def get_image(self, obj):
        image_field = getattr(obj, self.image_field_name, None)
        if image_field and hasattr(image_field, "url"):
            return mark_safe(
                f'<img src="{image_field.url}" style="border-radius: 50%;" width="50" height="50">'
            )
        return "Нет изображения"

    get_image.short_description = "Фото"


class SingletonAdminInfoMixin:
    """
    Миксин для отображения дополнительной информации в админке
    """

    singleton_info_text = "Можно создать только один экземпляр"
    singleton_info_color = "red"
    singleton_limit = 1

    def get_desc(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            self.singleton_info_color,
            self.singleton_info_text,
        )

    get_desc.short_description = "Доп Инфа"

    def has_add_permission(self, request):
        return self.model.objects.count() < self.singleton_limit


class AdminLimitMixin:
    """
    Миксин для ограничения количества экземпляров в админке
    """

    singleton_limit = 1

    def has_add_permission(self, request):
        return self.model.objects.count() < self.singleton_limit


class AdminShortDescriptionMixin:
    """
    Миксин для отображения короткого описания в админке
    """

    description_field_name = "description"
    description_length = 26

    def get_description(self, obj):
        value = getattr(obj, self.description_field_name, "")
        if not value:
            return "Нет описания"
        return f"{str(value)[:self.description_length]}..."

    get_description.short_description = "Описание"


class BaseSectionViewMixin(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        try:
            instance = self.model.objects.get()
        except self.model.DoesNotExist:
            raise NotFound(detail=f"{self.model.__name__} not found.")
        except MultipleObjectsReturned:
            raise NotFound(
                detail=f"Multiple {self.model.__name__} objects found. Only one expected."
            )

        serializer = self.serializer_class(instance)
        return Response(serializer.data)
