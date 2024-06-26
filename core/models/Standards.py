from django.conf import settings
from django.db import models

from sport_connect_api.models import BaseModel

__all__ = ('SportStandard',)


class SportStandard(BaseModel):
    name = models.CharField(max_length=225, verbose_name="Назва стандарту",
                            choices=((standard, standard) for standard in settings.LIST_STANDARDS), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Норматив"
        verbose_name_plural = "Нормативи"
