from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sports"
        verbose_name = "Вид спорту"
        verbose_name_plural = "Види спорту"


class SportSchool(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="sport_schools")
    school_name = models.CharField(max_length=350, null=False, blank=False)
    school_site_url = models.URLField(null=False, blank=False)
    school_sport_address = models.CharField(max_length=350, null=False, blank=False)
    school_sport_email = models.EmailField(null=True, blank=True)
    school_sport_phone_numbers = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.school_name

    class Meta:
        db_table = "sport_school"
        verbose_name = "Сайт ДЮСШ"
        verbose_name_plural = "Сайти ДЮСШ"


class AverageValuesStandards(models.Model):
    name_standard = models.CharField(max_length=225, verbose_name="Показник")
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


class WeightingFactors(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="weighting_factors")
    average_value_standard = models.ForeignKey(AverageValuesStandards, on_delete=models.CASCADE,
                                               related_name="weighting_factors")
    weighting_factor = models.FloatField(verbose_name="Ваговий коефіцієнт")

    class Meta:
        db_table = "weighting_factors"
        verbose_name = "Вагові коефіцієнти (за випробуваннями)"
        verbose_name_plural = "Вагові коефіцієнти (за випробуваннями)"



# class Exams(models.Model):

