from django.db import models

from config.models import BaseModel

__all__ = ('UserResult',)


class UserResult(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="user_results",
                             verbose_name="Користувач")
    result = models.JSONField(verbose_name="Результат")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    standards = models.JSONField(verbose_name="Виміри")

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результати"
