from django.db import models

from sport_connect_api.models import BaseModel

__all__ = ('WeightingFactors',)


class WeightingFactors(BaseModel):
    sport = models.ForeignKey('core.Sport', on_delete=models.CASCADE, related_name="weighting_factors",
                              verbose_name="Вид спорту")
    average_value_standard = models.ForeignKey('core.AverageValuesStandards', on_delete=models.CASCADE,
                                               related_name="weighting_factors", verbose_name="Норматив")
    weighting_factor = models.FloatField(verbose_name="Ваговий коефіцієнт")

    class Meta:
        db_table = "weighting_factors"
        verbose_name = "Вагові коефіцієнти (за випробуваннями)"
        verbose_name_plural = "Вагові коефіцієнти (за випробуваннями)"
