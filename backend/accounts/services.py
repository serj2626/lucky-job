from datetime import timedelta
from django.utils import timezone
from .models import EmailVerification
from .tasks import send_verification_email_task


def create_email_verification(user):
    # Удаляем старые неиспользованные записи
    user.email_verifications.filter(is_used=False).delete()

    expiration = timezone.now() + timedelta(hours=24)
    ev = EmailVerification.objects.create(user=user, expires_at=expiration)
    send_verification_email_task.delay(user.email, str(ev.token))
