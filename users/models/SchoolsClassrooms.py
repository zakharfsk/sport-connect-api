from django.db import models

from config.models import BaseModel
from users.querysets import SchoolClassesQuerySet

__all__ = ('SchoolsClassrooms',)


class SchoolsClassrooms(BaseModel):
    school = models.ForeignKey('users.Schools', on_delete=models.CASCADE)
    class_number = models.IntegerField(blank=False, null=True)
    class_letter = models.CharField(choices=(
        ('А', 'А'),
        ('Б', 'Б'),
        ('В', 'В'),
        ('Г', 'Г'),
        ('Д', 'Д'),
        ('Е', 'Е'),
        ('Ж', 'Ж'),
        ('З', 'З'),
        ('И', 'И'),
        ('К', 'К'),
        ('Л', 'Л'),
        ('М', 'М'),
        ('Н', 'Н'),
        ('О', 'О'),
        ('П', 'П'),
        ('Р', 'Р'),
        ('С', 'С'),
        ('Т', 'Т'),
        ('У', 'У'),
        ('Ф', 'Ф'),
        ('Х', 'Х'),
        ('Ц', 'Ц'),
        ('Ч', 'Ч'),
        ('Ш', 'Ш'),
        ('Щ', 'Щ'),
        ('Ь', 'Ь'),
        ('Ю', 'Ю'),
        ('Я', 'Я')
    ), max_length=1, blank=False, null=True)

    objects = SchoolClassesQuerySet.as_manager()

    def representation(self):
        return f'{self.class_number}-{self.class_letter}'

    def __str__(self):
        return f'{self.class_number}-{self.class_letter}'

    class Meta:
        db_table = 'schools_classrooms'
        verbose_name_plural = 'Класи'
        verbose_name = 'Клас'
