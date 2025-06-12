from celery import shared_task
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


@shared_task
def send_verification_email_task(email, token):
    url = f"{settings.SITE_URL}{reverse('verify_email', args=[token])}"
    subject = "Подтверждение почты"
    message = f"Здравствуйте!\n\nПерейдите по ссылке для подтверждения:\n{url}\n\nЕсли вы не регистрировались, проигнорируйте это письмо."

    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

    return True
