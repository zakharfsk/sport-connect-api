from django.db import models

from config.models import BaseModel

__all__ = ('WeightingFactors',)


class WeightingFactors(BaseModel):
    sport = models.ForeignKey('core.Sport', on_delete=models.CASCADE, related_name="weighting_factors",
                              verbose_name="Вид спорту")
    sport_standard = models.ForeignKey('core.SportStandard', on_delete=models.CASCADE,
                                               related_name="weighting_factors", verbose_name="Норматив")
    weighting_factor = models.FloatField(verbose_name="Ваговий коефіцієнт")

    def __str__(self):
        return f"{self.sport} - {self.sport_standard.name} - {self.weighting_factor}"

    class Meta:
        db_table = "weighting_factors"
        verbose_name = "Вагові коефіцієнти (за випробуваннями)"
        verbose_name_plural = "Вагові коефіцієнти (за випробуваннями)"
