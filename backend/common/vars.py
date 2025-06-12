WORK_SCHEDULE = (
    ("project", "Проектная работа"),
    ("full_time", "Полная занятость"),
    ("part_time", "Частичная занятость"),
    ("temporary", "Временная работа"),
    ("internship", "Стажировка"),
)

FORMAT_WORK = (
    ("office", "В офисе"),
    ("remote", "Удаленная работа"),
    ("hybrid", "Гибридная работа"),
)


LEVELS_REQUIREMENTS = (
    ("none", "Не имеет значения"),
    ("intern", "Стажер"),
    ("junior", "Junior"),
    ("junior_plus", "Junior+"),
    ("middle", "Middle"),
    ("middle_plus", "Middle+"),
    ("senior", "Senior"),
    ("team_lead", "Team Lead"),
)

STATUS_VACANCY = (
    ("open", " Открыта"),
    ("archived", "В архиве"),
)


CURRENCY_TYPE = (
    ("RUB", "руб"),
    ("USD", "долл"),
    ("EUR", "евро"),
)


SOCIAL_TYPES = (
    ("vk", "VK"),
    ("tg", "Telegram"),
    ("insta", "Instagram"),
    ("facebook", "Facebook"),
    ("linkedin", "LinkedIn"),
    ("twitter", "Twitter"),
    ("other", "Другое"),
)

CONTACT_TYPES = (
    ("phone", "Телефон"),
    ("email", "Почта"),
    ("skype", "Skype"),
    ("country", "Страна"),
    ("city", "Город"),
    ("address", "Адрес"),
    ("other", "Другое"),
)

MONTHS = (
    (1, "Январь"),
    (2, "Февраль"),
    (3, "Март"),
    (4, "Апрель"),
    (5, "Май"),
    (6, "Июнь"),
    (7, "Июль"),
    (8, "Август"),
    (9, "Сентябрь"),
    (10, "Октябрь"),
    (11, "Ноябрь"),
    (12, "Декабрь"),
)


STATUS_CHOICES = (
    ("pending", "На рассмотрении"),
    ("reviewed", "Просмотрено"),
    ("interview", "Приглашение на интервью"),
    ("rejected", "Отклонено"),
    ("hired", "Принято"),
)


CATEGORY_TYPES = (
    ("backend", "Бэкенд"),
    ("frontend", "Фронтенд"),
    ("fullstack", "Фулстайк"),
    ("analytics", "Аналитика"),
    ("devops", "DevOps"),
    ("design", "Дизайн"),
    ("other", "Другое"),
)