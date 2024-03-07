from django.db import models

from sport_connect_api.models import BaseModel

__all__ = ('SportSchool',)


class SportSchool(BaseModel):
    sport = models.ForeignKey('core.Sport', on_delete=models.CASCADE, related_name="sport_schools",
                              verbose_name="Вид спорту")
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
