from django.contrib.auth import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .services import create_email_verification
from django.conf import settings

from companies.models import Company
from specialists.models import Specialist

User = get_user_model()


# Статус пользователя
@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    user.online = True
    user.save()


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    user.online = False
    user.save()


# @receiver(post_save, sender=User)
# def user_created(sender, instance, created, **kwargs):
#     if created and not instance.is_verified:
#         create_email_verification(instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, created, **kwargs):
#     if instance.type == "Company" and created:
#         Company.objects.create(user=instance)
#     elif instance.type == "Employee" and created:
#         Employee.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    match instance.type:
        case "company":
            Company.objects.get_or_create(user=instance)
        case "specialists":
            Specialist.objects.get_or_create(user=instance)
        case "other" | "admin":
            pass
