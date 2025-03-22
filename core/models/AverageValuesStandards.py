from django.db import models

from config.models import BaseModel

__all__ = ('AverageValuesStandards',)


class AverageValuesStandards(BaseModel):
    standard = models.ForeignKey('core.SportStandard', on_delete=models.CASCADE, verbose_name="Показник")
    children_age = models.IntegerField(choices=[(i, i) for i in range(10, 12)], verbose_name="Вік дитини", null=True)
    children_gender = models.CharField(max_length=225, choices=[("Юнак", "Юнак"), ("Дівчина", "Дівчина")],
                                       verbose_name="Стать дитини", null=True)
    average_value = models.FloatField(verbose_name="Середнє значення", null=True)
    sigma = models.FloatField(verbose_name="Сигма")

    def __str__(self):
        return (f"Середнє значення по нормативу "
                f"\"{self.standard.name}\" "
                f"для дітей віку {self.children_age} років та статі {self.children_gender}")

    class Meta:
        db_table = "average_values_standards"
        verbose_name = "Середні значення по нормативах"
        verbose_name_plural = "Середні значення по нормативах"
