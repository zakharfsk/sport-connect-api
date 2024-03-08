from django.contrib import admin

from . import models


@admin.register(models.Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.SportSchool)
class SportSchoolAdmin(admin.ModelAdmin):
    list_display = ('sport', 'school_name', 'school_sport_address',
                    'school_sport_email')


@admin.register(models.AverageValuesStandards)
class AverageValuesStandardsAdmin(admin.ModelAdmin):
    list_display = ('name_standard', 'children_age', 'sigma')


@admin.register(models.WeightingFactors)
class WeightingFactorsAdmin(admin.ModelAdmin):
    list_display = ('sport', 'average_value_standard', 'weighting_factor')


@admin.register(models.UserResult)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'result', 'date_created', 'date_updated')
