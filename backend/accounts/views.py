# users/views.py
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import EmailVerification


def verify_email(request, token):
    ev = get_object_or_404(EmailVerification, token=token)

    if ev.is_used:
        messages.warning(request, "Ссылка уже использована.")
    elif ev.has_expired():
        messages.error(request, "Срок действия ссылки истёк.")
    else:
        ev.user.is_verified = True
        ev.user.save()
        ev.is_used = True
        ev.save()
        messages.success(request, "Email успешно подтверждён.")

    return redirect("login")  # можно изменить на нужный маршрут
