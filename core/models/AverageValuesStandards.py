from django.conf import settings
from django.db import models

from sport_connect_api.models import BaseModel

__all__ = ('AverageValuesStandards',)


class AverageValuesStandards(BaseModel):
    name_standard = models.CharField(max_length=225,
                                     choices=((standard, standard) for standard in settings.LIST_STANDARDS),
                                     verbose_name="Показник")
    children_age = models.IntegerField(choices=[(i, i) for i in range(10, 12)], verbose_name="Вік дитини", null=True)
    children_gender = models.CharField(max_length=225, choices=[("Юнак", "Юнак"), ("Дівчина", "Дівчина")],
                                       verbose_name="Стать дитини", null=True)
    average_value = models.FloatField(verbose_name="Середнє значення", null=True)
    sigma = models.FloatField(verbose_name="Сигма")

    # average_range = models.(verbose_name="Діапазон середнього значення", null=True)

    def __str__(self):
        return self.name_standard

    class Meta:
        db_table = "average_values_standards"
        verbose_name = "Середні значення по нормативах"
        verbose_name_plural = "Середні значення по нормативах"
