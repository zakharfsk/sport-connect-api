from django.contrib import admin

from . import models


class SportSchoolInline(admin.TabularInline):
    model = models.SportSchool
    extra = 0


@admin.register(models.Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [SportSchoolInline]


class AverageValuesStandardsAdmin(admin.TabularInline):
    model = models.AverageValuesStandards
    list_display = ('name_standard', 'children_age', 'children_gender', 'sigma')
    list_filter = (
        'name_standard',
        'children_age',
        'children_gender',
    )
    extra = 0


@admin.register(models.WeightingFactors)
class WeightingFactorsAdmin(admin.ModelAdmin):
    list_display = ('sport', 'average_value_standard', 'weighting_factor')


@admin.register(models.UserResult)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'result', 'date_created', 'date_updated')


@admin.register(models.SportStandard)
class SportStandardAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('averagevaluesstandards__children_age', 'averagevaluesstandards__children_gender')
    inlines = [AverageValuesStandardsAdmin]
