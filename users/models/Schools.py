from django.db import models

from config.models import BaseModel
from users.querysets import SchoolQuerySet

__all__ = ('Schools',)


class Schools(BaseModel):
    school_name = models.CharField(max_length=256, blank=False, null=False)
    school_city = models.CharField(max_length=256, blank=False, null=False)

    objects = SchoolQuerySet.as_manager()

    def __str__(self):
        return self.school_name

    class Meta:
        db_table = 'schools'
        verbose_name_plural = 'Школи'
        verbose_name = 'Школа'
