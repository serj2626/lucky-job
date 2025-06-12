from datetime import datetime
import os
from uuid import uuid4


def dynamic_upload_to(instance, filename):
    """
    Возвращает путь к загруженному файлу.
    """

    folder = instance.__class__.__name__.lower()
    ext = filename.split(".")[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join("uploads", folder, datetime.now().strftime("%Y/%m"), filename)
