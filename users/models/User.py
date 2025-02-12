from django.contrib.auth.models import AbstractUser
from django.db import models

from config.models import BaseModel

__all__ = ('User',)


class User(AbstractUser, BaseModel):
    user_school = models.ForeignKey('users.Schools', on_delete=models.CASCADE, blank=True, null=True)
    user_classroom = models.ForeignKey('users.SchoolsClassrooms', on_delete=models.CASCADE, blank=True, null=True)
    user_gender = models.CharField(choices=(
        ('Дівчина', 'Дівчина'),
        ('Юнак', 'Юнак')),
        max_length=256, blank=True, null=True)
    user_age = models.IntegerField(choices=((10, 10), (11, 11)), blank=True, null=True)
    fcm_token = models.CharField(max_length=256, blank=True, null=True)

    def to_xlsx_format(self):
        return {
            'id': self.id,
            'Ім\'я': self.first_name,
            'Прізвище': self.last_name,
            'Стать': self.user_gender,
            'Вік': self.user_age,
            'Школа': self.user_school.school_name,
            'Клас': f'{self.user_classroom.representation()}'
        }

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Користувачі'
        verbose_name = 'Користувач'
