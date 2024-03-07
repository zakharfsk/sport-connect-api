from django.db import models

from sport_connect_api.models import BaseModel

__all__ = ('Sport',)


class Sport(BaseModel):
    name = models.CharField(max_length=225, verbose_name="Вид спорту")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sports"
        verbose_name = "Вид спорту"
        verbose_name_plural = "Види спорту"
