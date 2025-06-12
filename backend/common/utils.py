from django.utils.text import slugify


def get_client_ip(request):
    """
    Функция для получения IP-адреса клиента
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_new_slug(title: str) -> str:
    return slugify(title)
