from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid
from common.models import BaseID
from datetime import timedelta

EXPIRE_MONUTE = 60


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(BaseID, AbstractBaseUser, PermissionsMixin):
    image_field_name = "avatar"

    USER_TYPE_CHOICES = (
        ("company", "Компания"),
        ("specialists", "Специалист"),
        ("other", "Другой"),
        ("admin", "Администратор"),
    )

    email = models.EmailField(unique=True, verbose_name="Почта")
    type = models.CharField(
        max_length=255,
        choices=USER_TYPE_CHOICES,
        default="employee",
        verbose_name="Тип",
    )
    online = models.BooleanField(default=False, verbose_name="онлайн")
    is_verified = models.BooleanField(default=False, verbose_name="подтвержден")
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.type = "admin"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.get_type_display()} ({self.email})"


class EmailVerification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="email_verifications",
        verbose_name="Пользователь",
    )
    token = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, verbose_name="Токен"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    expires_at = models.DateTimeField("Дата истечения", blank=True, null=True)

    is_used = models.BooleanField(default=False, verbose_name="использован")

    def has_expired(self):
        return timezone.now() > self.expires_at

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=EXPIRE_MONUTE)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {'used' if self.is_used else 'pending'}"
