from django.conf import settings
from django.db import models

from sport_connect_api.models import BaseModel


class Sport(BaseModel):
    name = models.CharField(max_length=225, verbose_name="Вид спорту")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sports"
        verbose_name = "Вид спорту"
        verbose_name_plural = "Види спорту"


class SportSchool(BaseModel):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="sport_schools", verbose_name="Вид спорту")
    school_name = models.CharField(max_length=350, null=False, blank=False, verbose_name="Назва ДЮСШ")
    school_site_url = models.URLField(null=False, blank=False, verbose_name="Сайт ДЮСШ")
    school_sport_address = models.CharField(max_length=350, null=False, blank=False, verbose_name="Адреса ДЮСШ")
    school_sport_email = models.EmailField(null=True, blank=True, verbose_name="Електронна адреса ДЮСШ")
    school_sport_phone_numbers = models.CharField(max_length=500, null=True, blank=True, verbose_name="Телефони ДЮСШ")

    def __str__(self):
        return self.school_name

    class Meta:
        db_table = "sport_school"
        verbose_name = "Сайт ДЮСШ"
        verbose_name_plural = "Сайти ДЮСШ"


class AverageValuesStandards(BaseModel):
    name_standard = models.CharField(max_length=225,
                                     choices=((standard, standard) for standard in settings.LIST_STANDARDS),
                                     verbose_name="Показник")
    children_age = models.IntegerField(choices=[(i, i) for i in range(10, 12)], verbose_name="Вік дитини", null=True)
    children_gender = models.CharField(max_length=225, choices=[("Юнак", "Юнак"), ("Дівчина", "Дівчина")],
                                       verbose_name="Стать дитини", null=True)
    average_value = models.FloatField(verbose_name="Середнє значення", null=True)
    sigma = models.FloatField(verbose_name="Сигма")

    def __str__(self):
        return self.name_standard

    class Meta:
        db_table = "average_values_standards"
        verbose_name = "Середні значення по нормативах"
        verbose_name_plural = "Середні значення по нормативах"


class WeightingFactors(BaseModel):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="weighting_factors",
                              verbose_name="Вид спорту")
    average_value_standard = models.ForeignKey(AverageValuesStandards, on_delete=models.CASCADE,
                                               related_name="weighting_factors", verbose_name="Норматив")
    weighting_factor = models.FloatField(verbose_name="Ваговий коефіцієнт")

    class Meta:
        db_table = "weighting_factors"
        verbose_name = "Вагові коефіцієнти (за випробуваннями)"
        verbose_name_plural = "Вагові коефіцієнти (за випробуваннями)"
